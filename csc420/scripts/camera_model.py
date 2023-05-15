import cv2
import numpy as np
from matplotlib import pyplot as plt

def imshow(img, ax=None, title="", bgr=True):
    # since plt and cv2 have different RGB sorting
    if bgr:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    if ax == None:
        plt.imshow(img.astype(np.uint8))
        plt.axis("off")
        plt.title(title)
    else:
        ax.imshow(img.astype(np.uint8))
        ax.set_axis_off()
        ax.set_title(title)
        
Ms = [
    np.array([
        [1, 0, 0], 
        [0, 1.,0]
    ]),
    np.array([
        [1, 0, 20], 
        [0, 1., 20]
    ]),
    np.array([
        [np.cos(0.5), np.sin(0.5), 0], 
        [-np.sin(0.5), np.cos(0.5), 20]
    ]),
    np.array([
        [np.cos(0.5), np.sin(0.5), 0], 
        [-np.sin(0.5), np.cos(0.5), 0]
    ]) * 0.5,
    np.array([
        [1, 0.2, -5], 
        [0.3, 1.3, -5]
    ])
]
titles = ["Origin", "Translation", "Rigid", "Similarity", "Affine"]
Mstr = [
    "1. 0. 1.\n 0. 1. 0.", "1. 0. 20.\n0. 1. 20.", 
    " cos(0.5) sin(0.5)  0\n-sin(0.5) cos(0.5) 20", 
    " 0.5cos(0.5) 0.5sin(0.5) 0\n-0.5sin(0.5) 0.5cos(0.5) 0",
    "  1 0.2 -5.\n0.3 1.3 -5."
]
plt.figure(figsize=(8, 6.5))
img = np.zeros((100, 100))
img[33:66, 33:66] = 1
for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i] + "\n" + Mstr[i])
    plt.axis("off")
    plt.imshow(cv2.warpAffine(img, Ms[i], (100, 100)), cmap="Greens")
plt.subplot(236)
plt.axis("off")

plt.savefig("../assets/camera_model.jpg")