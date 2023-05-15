import cv2
import numpy as np
import matplotlib.pyplot as plt

image_sq = cv2.imread('../assets/blue-square.png', cv2.IMREAD_GRAYSCALE)
image_yu = cv2.imread('../assets/yurina.jpg', cv2.IMREAD_GRAYSCALE)
H, W = image_yu.shape
image_sq = cv2.resize(image_sq, (W, H))
F_dx = np.array([[-1, 1]])
F_dy = F_dx.T

image = np.vstack((image_sq, image_yu))
output = np.hstack([
    image, 
    cv2.filter2D(image, -1, F_dx, delta=122),
    cv2.filter2D(image, -1, F_dy, delta=122)
])
output = cv2.putText(output, "original", (0, 20),cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
output = cv2.putText(output, "[-1, 1]", (W, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
output = cv2.putText(output, "[-1, 1].T", (W*2, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
cv2.imwrite('../assets/edge_detection_1.jpg', output)

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
sobel_y = sobel_x.T
output = np.hstack([
    image_yu, 
    cv2.filter2D(image_yu, -1, sobel_x, delta=122),
    cv2.filter2D(image_yu, -1, sobel_y, delta=122)
])
output = cv2.putText(output, "original", (0, 20),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
output = cv2.putText(output, "Sobel x, size=3", (W, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
output = cv2.putText(output, "Sobel y, size=3", (W*2, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
cv2.imwrite('../assets/edge_detection_sobel.jpg', output)


rand = 60 + np.random.rand(500) * 5
rand = np.append(rand, np.arange(65, 35, -3))
rand = np.append(rand, 30 + np.random.rand(500) * 5)
ksize, sigma = 11, 5
kernel = cv2.getGaussianKernel(ksize, sigma)
smoothed = np.array([np.dot(kernel.T, rand[i:i+ksize]) for i in range(len(rand) - ksize)])
fig, axs = plt.subplots(2, 2, figsize=(6, 5))
axs[0][0].plot(rand)
axs[0][0].set_title("f(x)")
axs[0][1].plot(rand[1:] - rand[:-1])
axs[0][1].set_title("d/dx f(x)")
axs[1][0].plot(smoothed)
axs[1][0].set_title("smoothed with Gaussian h")
axs[1][1].plot(smoothed[1:] - smoothed[:-1])
axs[1][1].set_title("d/dx h * f");
fig.tight_layout()
fig.savefig("../assets/edge_detection_noise.jpg")

cannys = []
fig, axs = plt.subplots(3, 3, figsize=(12, 12))
for i in range(3):
    for j in range(3):
        low = 10 + i * 30
        high = 100 + j * 50
        img = np.ones((H + 22, W)) * 255
        img[22:, :] = cv2.Canny(image_yu, low, high)
        cv2.putText(img, f"low={low}, high={high}", 
                    (0, 20),cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 1)
        cannys.append(img)
cannys = np.vstack([
    np.hstack(cannys[:3]),
    np.hstack(cannys[3:6]),
    np.hstack(cannys[6:])
])
cv2.imwrite("../assets/edge_detection_canny.jpg", cannys)


rand = 60 + np.random.rand(500)
rand = np.append(rand, np.arange(60, 0, -5))
rand = np.append(rand, np.random.rand(500))
ksize, sigma = 51, 5
kernel = cv2.getGaussianKernel(ksize, sigma)

smoothed = np.array([np.dot(kernel.T, rand[i:i+ksize]) for i in range(len(rand) - ksize)])
d_smoothed = smoothed[1:] - smoothed[:-1]
fig, axs = plt.subplots(1, 2, figsize=(7, 3))
axs[0].plot(rand)
axs[0].set_title(r"$f(x)$")
axs[1].plot(d_smoothed[1:] - d_smoothed[:-1])
axs[1].set_title(r"$\frac{d^2}{dx^2} h \cdot f$")
fig.tight_layout()
fig.savefig("../assets/edge_detection_log.jpg")