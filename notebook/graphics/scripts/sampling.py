
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import cv2


def DFT(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    mag = np.abs(fshift)
    return (mag - mag.min()) / (mag.max() - mag.min())
     

size = 100
x = np.linspace(-size, size, size)
y = np.linspace(-size, size, size)
xv, yv = np.meshgrid(x, y)

# constant image
imgs = [
    (np.ones((size, size)) / 2, "constant"),
    (np.sin(np.pi / 16 * xv), r"$\sin(2\pi\frac{1}{16}x)$"),
    (np.sin(np.pi / 8 * yv), r"$\sin(2\pi\frac{1}{8}y)$"),
    (np.sin(np.pi / 16 * xv) * np.sin(np.pi / 8 * yv), 
        r"$\sin(2\pi\frac{1}{16}x) \sin(2\pi\frac{1}{8}y)$"),
    (np.sin(np.pi / 16 * xv) + np.sin(np.pi / 8 * yv), 
        r"$\sin(2\pi\frac{1}{16}x) + \sin(2\pi\frac{1}{8}y)$"),
    (np.exp(-(xv*xv + yv*yv) / 256), r"Gaussian, $\sigma=1/16$"),
    (np.exp(-(xv*xv + yv*yv) / (32 * 32)), r"Gaussian, $\sigma=1/32$"),
    (np.exp(-(xv*xv) / (32 * 32)) * np.exp(-(yv*yv) / (16 * 16)) , r"Gaussian, $\sigma=[1/16, 1/32]$")
]

plt.figure(figsize=(12, 12))
for i, img_t in enumerate(imgs):
    img, title = img_t
    plt.subplot(4, 2, i+1)
    plt.imshow(np.hstack((img, DFT(img))), cmap="gray")
    plt.title(title)
    plt.axis("off")
plt.tight_layout()
plt.savefig("../assets/fft.jpg")


def visualize_ft(fshift):
    mag = 20 * np.log1p(np.abs(fshift))
    mag = (mag - mag.min()) / (mag.max() - mag.min())
    return (mag * 255).astype(np.uint8)
    
inverse_fft = lambda fshift: np.real(np.fft.ifft2(np.fft.ifftshift(fshift))).astype(np.uint8)

img = cv2.cvtColor(cv2.imread("../assets/yurina.jpg"), cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (200, 200))
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
filter_high_pass = cv2.circle(np.zeros((200, 200)), (100, 100), 25, 1, -1)
fshift_high_pass = fshift * filter_high_pass

filter_low_pass = cv2.circle(np.ones((200, 200)), (100, 100), 10, 0, -1)
fshift_low_pass = fshift * filter_low_pass

filter_lap = cv2.circle(np.zeros((200, 200)), (100, 100), 50, 1, -1)
filter_lap = cv2.circle(filter_lap, (100, 100), 25, 0, -1)
fshift_lap = fshift * filter_lap

img_out = [
    [img, visualize_ft(fshift)],
    [inverse_fft(fshift_high_pass), visualize_ft(fshift_high_pass)],
    [inverse_fft(fshift_low_pass), visualize_ft(fshift_low_pass)],
    [inverse_fft(fshift_lap), visualize_ft(fshift_lap)],
]

img_out = [np.vstack(imgs) for imgs in img_out]
img_out = np.hstack(img_out)
cv2.imwrite("../assets/convolution_thrm.jpg", img_out)