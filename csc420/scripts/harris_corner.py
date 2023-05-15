import cv2
import numpy as np
import plotly.express as px

img = cv2.imread("../assets/Corners.jpg", cv2.IMREAD_GRAYSCALE).astype(float)
img_blurred = cv2.GaussianBlur(img, (3, 3), 1)

def to_image(data):
    return (255 * (data - data.min()) / (data.max() - data.min())).astype(np.uint8)

F_dx = np.array([[-1, 1]])
F_dy = F_dx.T

img_dx = cv2.filter2D(img_blurred, -1, F_dx, delta=122)
img_dy = cv2.filter2D(img_blurred, -1, F_dy, delta=122)


output = np.vstack([
    np.hstack([to_image(img_blurred), to_image(img_dx), to_image(img_dy)]),
    np.hstack([to_image(img_dx * img_dy), to_image(img_dx * img_dx), to_image(img_dy * img_dy)]),
])
cv2.imwrite("../assets/harris_corner_1.jpg", output)

patch = img[300: 350, 50: 100]
I_x = cv2.filter2D(patch, -1, np.array([[-1, 1]]))
I_y = cv2.filter2D(patch, -1, np.array([[-1], [1]]))

M = np.array([[np.sum(I_x ** 2), np.sum(I_x * I_y)], 
              [np.sum(I_x * I_y), np.sum(I_y ** 2)]])
us, vs = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
vec = np.empty((20, 20, 1, 2))
vec[:, :, 0, 0] = us
vec[:, :, 0, 1] = vs
vec_t = np.transpose(vec, (0,1,3,2))

fig = px.imshow((vec @ M @ vec_t)[:, :, 0, 0])
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)
with open("../assets/harris_corner_wssd.json", "w") as f:
    f.write(fig.to_json())
    
patches_starts = [(300, 50), (30, 10), (130, 330)]
patch_size = 40
output = img.copy()
for y, x in patches_starts:
    patch = img[y:y+patch_size, x:x+patch_size]
    output = cv2.rectangle(
        output, 
        (x, y), (x+patch_size, y+patch_size), 
        (127, 127, 127), 2
    )
    I_x = cv2.filter2D(patch, -1, np.array([[-1, 1]]))
    I_y = cv2.filter2D(patch, -1, np.array([[-1], [1]]))

    M = np.array([[np.sum(I_x ** 2), np.sum(I_x * I_y)], 
                [np.sum(I_x * I_y), np.sum(I_y ** 2)]])
    
    eig = np.round(np.linalg.eigvals(M), 2)
    R = eig[0] * eig[1] - 0.04*(eig[0] + eig[1])**2
    output = cv2.putText(output, f"lmbd=({eig[0]},{eig[1]})", 
                (x, y-2),cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
    output = cv2.putText(output, f"R={R}", 
                (x, y-12),cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
cv2.imwrite("../assets/harris_corner.jpg", output)