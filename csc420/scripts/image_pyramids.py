import cv2
import numpy as np
import plotly.graph_objects as go

img = cv2.imread("../assets/yurina.jpg")

H, W, C = img.shape
output = np.zeros((H, W * 3, C), dtype=np.uint8)
output[:, :W, :] = img
output[:, W:2*W, :] = cv2.resize(img[::2,::2,:], (W, H), interpolation=cv2.INTER_NEAREST)
output[:, 2*W:, :] = cv2.resize(img[::4,::4,:], (W, H), interpolation=cv2.INTER_NEAREST)
cv2.imwrite("../assets/image_downsample.jpg", output)


img2 = cv2.imread("../assets/window.jpg")
img2 = cv2.resize(img2, (W, H))
output = np.empty((H, W*2, 3), dtype=np.uint8)
for i in range(img.shape[1]):
    output[:, 2*i] = img2[:, i]
    output[:, 2*i+1] = img[:, i]
cv2.imwrite("../assets/image_downsample_2.jpg", output)



x = np.arange(0, 40, 0.2)
x2 = np.arange(0, 40, 3)
fig = go.Figure(data=[
    go.Scatter(x=x, y=np.cos(x), name="sample rate=0.2"),
    go.Scatter(x=x2,y=np.cos(x2), name="sample rate=3")
])
with open("../assets/nyquist_cos.json", "w") as f:
    f.write(fig.to_json())

img3 = cv2.GaussianBlur(output, (3, 3), 3)[:, ::2]
cv2.imwrite("../assets/image_downsample_3.jpg", img3)
