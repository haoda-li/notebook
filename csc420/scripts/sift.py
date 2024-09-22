import cv2
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


image_window = cv2.imread("../assets/window.jpg", cv2.IMREAD_GRAYSCALE).astype(float)
H, W = image_window.shape
# --8<-- [start:octave]
def construct_octaves(image, n_octaves: int, s: int, sigma: float):
    """
    image: the original image
    n_octaves: number of octaves
    s: down sampling rate
    sigma: scale
    """
    octaves = []
    for _ in range(n_octaves):
        octave = [image.copy()]
        for _ in range(s - 1):
            image = cv2.GaussianBlur(image, (5, 5), sigma)
            octave.append(image.copy())
        image = image[::2,::2]
        octaves.append(octave)
        
    return octaves
# --8<-- [end:octave]
n_octaves = 3
s = 5
sigma = 2 ** 0.5
octaves = construct_octaves(image_window, n_octaves, s, sigma)
output = np.ones((sum([octave[0].shape[0] for octave in octaves]), W * s), dtype=np.uint8) * 255
start_height = 0
for oct in octaves:
    row = np.hstack(oct)
    end_height = start_height + row.shape[0]
    output[start_height:end_height,:row.shape[1]] = row
    start_height = end_height
cv2.imwrite("../assets/sift_octave.jpg", output[::2, ::2])

# --8<-- [start:dog]
DoGs = [
    [octave[i] - octave[i-1] for i in range(1, len(octave))]
    for octave in octaves
]
# --8<-- [end:dog]
output = np.ones((sum([octave[0].shape[0] for octave in octaves]), W * (s-1)), dtype=np.uint8) * 255
start_height = 0
for oct in DoGs:
    row = np.hstack(oct)
    row = 255 * (row - row.min()) / (row.max() - row.min())
    end_height = start_height + row.shape[0]
    output[start_height:end_height,:row.shape[1]] = row
    start_height = end_height
cv2.imwrite("../assets/sift_dog.jpg", output[::2, ::2])

# --8<-- [start:extrema]
def find_local_extrema(above, self, below):
    """ Find the local extrema contained in self"""
    key_points = []
    rows, cols = self.shape
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            window = np.empty((3, 3, 3))
            window[:, :, 0] = above[r-1: r+2, c-1: c+2]
            window[:, :, 1] = self[r-1: r+2, c-1: c+2]
            window[:, :, 2] = below[r-1: r+2, c-1: c+2]
            if self[r, c] == np.max(window) or self[r, c] == np.min(window):
                key_points.append((r, c))
    return key_points
# --8<-- [end:extrema]