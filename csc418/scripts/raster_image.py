import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

bayer_filter = np.zeros((10, 20, 3), dtype=np.uint8)
bayer_filter[::2, ::2, 1] = 255
bayer_filter[1::2, 1::2, 1] = 255
bayer_filter[::2, 1::2, 0] = 255
bayer_filter[1::2, ::2, 2] = 255

fig = px.imshow(bayer_filter, title="Bayer filter")
with open("../assets/bayer.json", "w") as f:
    f.write(fig.to_json())
    
# --8<-- [start:bayer]
def simulate_bayer_filter(image):
    output = np.empty(image.shape[:2])
    output[::2, ::2] = image[::2, ::2, 1] 
    output[1::2, 1::2] = image[1::2, 1::2, 1]
    output[::2, 1::2] = image[::2, 1::2, 0]
    output[1::2, ::2] = image[1::2, ::2, 2]
    return output
# --8<-- [end:bayer]

# --8<-- [start:demosaic]
def demosaic(image):
    corner_kernel = np.array([[.25, 0, .25], 
                              [0,   0, 0], 
                              [.25, 0, .25]])
    cross_kernel = np.array([[0.,  .25, 0. ], 
                             [.25, 0.,  .25], 
                             [0.,  .25, 0. ]])
    h_kernel = np.array([[.5, 0., .5]])
    v_kernel = h_kernel.T
    
    output = np.empty(list(image.shape) + [3])
    
    # fill in the R value
    # if bayer pixel is red, take self
    output[::2, 1::2, 0] = image[::2, 1::2]
    # if bayer pixel is green, 
    output[::2, ::2, 0] = convolve2d(image, h_kernel, mode="same")[::2, ::2]
    output[1::2, 1::2, 0] = convolve2d(image, v_kernel, mode="same")[1::2, 1::2]
    # if bayer pixel is blue, take corners
    output[1::2, ::2, 0] = convolve2d(image, corner_kernel, mode="same")[1::2, ::2]
    
    # fill in the G value
    # if bayer pixel is red or blue, take the cross
    output[::2, 1::2, 1] = convolve2d(image, cross_kernel, mode="same")[::2, 1::2]
    output[1::2, ::2, 1] = convolve2d(image, cross_kernel, mode="same")[1::2, ::2]
    # if bayer pixel is green, take self
    output[::2, ::2, 1] = image[::2, ::2]
    output[1::2, 1::2, 1] = image[1::2, 1::2]
    
    # fill in the blue value
    # if bayer pixel is red, take corners
    output[::2, 1::2, 2] = convolve2d(image, corner_kernel, mode="same")[::2, 1::2]
    # if bayer pixel is green. take top and botton neightbors
    output[::2, ::2, 2] = convolve2d(image, v_kernel, mode="same")[::2, ::2]
    output[1::2, 1::2, 2] = convolve2d(image, h_kernel, mode="same")[1::2, 1::2]
    # if bayer pixel is blue, take self
    output[1::2, ::2, 2] = image[1::2, ::2]
    return output.astype(np.uint8)
# --8<-- [end:demosaic]

image = plt.imread("../assets/yurina.jpg")
bayered = simulate_bayer_filter(image)
demosed = demosaic(bayered)

plt.figure(figsize=(8.5, 3))
plt.subplot(131); plt.imshow(image); plt.title("Original"); plt.axis("off")
plt.subplot(132); plt.imshow(bayered, cmap="gray"); plt.title("Simulated Bayer Filter");  plt.axis("off")
plt.subplot(133); plt.imshow(demosed); plt.title("Demosed Image");  plt.axis("off")
plt.tight_layout();
plt.savefig("../assets/demosaic.jpg")

# --8<-- [start:color]
def rgb2hsv(image):
    output = np.zeros(image.shape)
    if image.dtype == np.uint8:
        image = image.astype(float) / 255
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    c_max = np.max(image, axis=2)
    c_min = np.min(image, axis=2)
    delta = c_max - c_min
    r_indice = np.logical_and(c_max == r, delta > 0)
    output[r_indice, 0] = 60 * ((g[r_indice] - b[r_indice]) / delta[r_indice])

    g_indice = np.logical_and(c_max == g, delta > 0)
    output[g_indice, 0] = 60 * ((b[g_indice] - r[g_indice]) / delta[g_indice] + 2)

    b_indice = np.logical_and(c_max == b, delta > 0)
    output[b_indice, 0] = 60 * ((r[b_indice] - g[b_indice]) / delta[b_indice] + 4)
    
    output[:, :, 0] = np.mod(output[:, :, 0], 360)

    output[c_max > 0, 1] = delta[c_max > 0] / c_max[c_max > 0]
    output[:, :, 2] = c_max
    return output

def hsv2rgb(image):
    h, s, v = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    c = v * s
    x = c * (1 - np.abs(np.mod(h/60, 2) - 1))
    m = v - c
    
    rgb = np.zeros(image.shape)
    
    cond = np.logical_and(h >= 0, h < 60)
    rgb[cond, 0] = c[cond]
    rgb[cond, 1] = x[cond]
    
    cond = np.logical_and(h >= 60, h < 120)
    rgb[cond, 0] = x[cond]
    rgb[cond, 1] = c[cond]
    
    cond = np.logical_and(h >= 120, h < 180)
    rgb[cond, 1] = c[cond]
    rgb[cond, 2] = x[cond]
    
    cond = np.logical_and(h >= 180, h < 240)
    rgb[cond, 1] = x[cond]
    rgb[cond, 2] = c[cond]
    
    cond = np.logical_and(h >= 240, h < 300)
    rgb[cond, 0] = x[cond]
    rgb[cond, 2] = c[cond]
    
    cond = np.logical_and(h >= 300, h <= 360)
    rgb[cond, 0] = c[cond]
    rgb[cond, 2] = x[cond]
    
    return np.round(255 * (rgb + m[:, :, np.newaxis])).astype(np.uint8)
# --8<-- [end:color]

image = plt.imread("../assets/yurina.jpg")
hsv_image = rgb2hsv(image)

fig = make_subplots(1, 3, shared_xaxes=True, shared_yaxes=True)
plt.figure(figsize=(8.5, 3))
plt.subplot(131); plt.imshow(hsv_image[:,:,0], cmap="gray"); plt.title("Hue"); plt.axis("off")
plt.subplot(132); plt.imshow(hsv_image[:,:,1], cmap="gray"); plt.title("Saturation");  plt.axis("off")
plt.subplot(133); plt.imshow(hsv_image[:,:,2], cmap="gray"); plt.title("Value");  plt.axis("off");
plt.tight_layout()
plt.savefig("../assets/hsv.jpg")

# --8<-- [start:edit]
def hue_shift(image, shift):
    output = image.copy()
    output[:, :, 0] = np.mod(output[:, :, 0] + shift, 360)
    return output

def saturate_change(image, factor):
    output = image.copy()
    output[:, :, 1] = np.clip(output[:, :, 1] * (1 + factor), 0, 1)
    return output

def lightness_change(image, factor):
    output = image.copy()
    output[:, :, 2] = np.clip(output[:, :, 2] * (1 + factor), 0, 1)
    return output
# --8<-- [end:edit]


fig, axes = plt.subplots(3, 3, figsize=(9, 10))
images = [
    [hsv2rgb(hue_shift(hsv_image, -30)), image, hsv2rgb(hue_shift(hsv_image, 30))],
    [hsv2rgb(saturate_change(hsv_image, -.5)), image, hsv2rgb(saturate_change(hsv_image, .5))],
    [hsv2rgb(lightness_change(hsv_image, -.5)), image, hsv2rgb(lightness_change(hsv_image, .5))]
]
titles = [
    ["Hue shift by -30", "Original", "Hue shift by 30"],
    ["Desaturate by 50%", "Original", "Saturate by 50%"],
    ["Darken by 50%", "Original", "Lit by 50%"]
]
for row in range(3):
    for col in range(3):
        axes[row][col].imshow(images[row][col])
        axes[row][col].set_axis_off()
        axes[row][col].set_title(titles[row][col])
fig.tight_layout()
fig.savefig("../assets/edit.jpg")