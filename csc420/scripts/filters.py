import cv2
import numpy as np
from scipy.signal import convolve2d

# load as gray scale
img_gray = cv2.imread("../assets/yurina.jpg", cv2.IMREAD_GRAYSCALE)
# load as colored
img = cv2.imread("../assets/yurina.jpg")

# --8<-- [start:shift]
# shift down by 25px
k_shifting = np.zeros((50, 50))
k_shifting[0, 24] = 1
# --8<-- [end:shift]
img_shifting = cv2.filter2D(img, -1, k_shifting, borderType=cv2.BORDER_CONSTANT)
cv2.imwrite("../assets/filter_shift.jpg", np.hstack((img, img_shifting)))

# --8<-- [start:sharpen]
k_sharp_3_2 = - np.ones((3,3), np.float32) / 9
k_sharp_3_2[1,1] = 2
k_sharp_3_2 = k_sharp_3_2 

k_sharp_3_5 = - np.ones((3,3), np.float32) *4 / 9
k_sharp_3_5[1,1] = 5

k_sharp_5_5 = - np.ones((5,5), np.float32) *4 / 25
k_sharp_5_5[2,2] = 5
# --8<-- [end:sharpen]

img_sharp_3_2 = cv2.filter2D(img, -1, k_sharp_3_2)
img_sharp_3_5 = cv2.filter2D(img, -1, k_sharp_3_5)
img_sharp_5_5 = cv2.filter2D(img, -1, k_sharp_5_5)

cv2.imwrite("../assets/filter_sharpen.jpg", np.hstack((img_sharp_3_2, img_sharp_3_5, img_sharp_5_5)))

# --8<-- [start:average]
k_3 = np.ones((3,3),np.float32) / 9
k_5 = np.ones((5,5),np.float32) / 25
k_11 = np.ones((11,11),np.float32) / 121
# --8<-- [end:average]

img_3 = cv2.filter2D(img,-1,k_3)
img_5 = cv2.filter2D(img,-1,k_5)
img_11 = cv2.filter2D(img,-1,k_11)

cv2.imwrite("../assets/filter_ave.jpg", np.hstack((img_3, img_5, img_11)))

# --8<-- [start:gauss]
# simple version of a square Gaussian function
# this filter is equivalent to cv2.GaussianBlur(img, (size, size), sigma)
def Gaussian(size, sigma):
    coef = 1 / (2 * np.pi * sigma **2)
    gaus = np.fromfunction(lambda x, y: coef * np.e \
                           ** ((-1*((x-(size-1)/2)**2+(y-(size-1)/2)**2))/(2*sigma**2)), (size, size))
    return gaus / np.sum(gaus)
# --8<-- [end:gauss]

smoothed = []
for size in [5, 10, 15]:
    row = []
    for sigma in [1, 3, 5]:
        title = f"fsize={size}, sigma={sigma}"
        temp = cv2.filter2D(img, -1, Gaussian(size, sigma))
        temp = cv2.putText(temp, title, (10, 10),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
        row.append(temp)
    smoothed.append(np.hstack(row))
cv2.imwrite("../assets/filter_gaussian.jpg", np.vstack(smoothed))
# --8<-- [start:match]
def findMatch(crop, target):
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY).astype(float)
    crop = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY).astype(float)
    H_crop, W_crop = crop.shape[:2]
    ave_kernel = np.ones((H_crop, W_crop)) / (H_crop * W_crop)
    kNorm = (np.sum(crop * crop)) ** 0.5
    targetNorm = np.sqrt(cv2.filter2D(target * target, -1, ave_kernel) * (H_crop * W_crop))
    conv = cv2.filter2D(target, -1, crop / kNorm)
    return conv / targetNorm
# --8<-- [end:match]    
img_crop = img.copy()
cv2.rectangle(img_crop, (15, 35), (65, 85), 255)

crop = img[35: 85, 15: 65]
matched = findMatch(crop, img) * 255
cv2.rectangle(matched, (15, 35), (65, 85), 255)
cv2.imwrite(
    "../assets/filter_match.jpg", 
    np.hstack((img_crop, np.tile(matched[:, :, None], 3)))
)

# --8<-- [start:sep]   
kernel = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])
kernel_h = np.array([[-1, 0, 1]])
kernel_v = np.array([[1, 2, 1]]).T
# note that images are in uint8
# and the 1D filters are not normalized
img_gray = img_gray.astype(float)
img_k = cv2.filter2D(img_gray, -1, kernel)
img_k1 = cv2.filter2D(img_gray, -1, kernel_h)
img_k2 = cv2.filter2D(img_k1, -1, kernel_v)

print(np.max(np.abs(img_k - img_k2)))
#>> 0.0
# --8<-- [end:sep]   
cv2.putText(img_k, f"Sobel_x 3*3", 
                    (20, 200),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
cv2.putText(img_k1, f"h", 
                    (20, 200),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)
cv2.putText(img_k2, f"v * h", 
                    (20, 200),cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 1)


cv2.imwrite("../assets/filter_sep.jpg", np.hstack((img_k, img_k1, img_k2)))