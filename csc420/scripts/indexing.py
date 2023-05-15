import cv2
import numpy as np
from sklearn.cluster import KMeans
import requests
from tqdm import tqdm

import os

sift = cv2.SIFT_create()

# --8<-- [start:dataset]
def make_dataset(N=100, load_dir=None, save_dir=None):
    """ N: the number of images for the dataset
        return a database of N images and their keypoints and descriptors 
    """
    images = []
    keypoints = []
    descriptors = []
    
    if load_dir:
        for path in os.listdir(load_dir):
            image = cv2.imread(os.path.join(load_dir, path))
            kps, des = sift.detectAndCompute(image, None)
            images.append(image)
            keypoints.append(kps)
            descriptors.append(des)
        return images, keypoints, descriptors
    
    # https://picsum.photos/ will return random images 
    url = "https://picsum.photos/200/"
    for i in tqdm(range(N)):
        kps = None
        while not kps:
            image = np.asarray(bytearray(requests.get(url).content), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            kps, des = sift.detectAndCompute(image, None)
        if save_dir:
            cv2.imwrite(os.path.join(save_dir, f"{i}.png"), image)
        images.append(image)
        keypoints.append(kps)
        descriptors.append(des)
    return images, keypoints, descriptors
# --8<-- [end:dataset]
images, kps, descriptors = make_dataset(50);


first_20_images = np.vstack([
    np.hstack(images[0:5]), 
    np.hstack(images[5:10]), 
    np.hstack(images[10:15]),
    np.hstack(images[15:20])
])
first_20_images = cv2.resize(first_20_images, (500, 400))
cv2.imwrite("../assets/indexing_example.jpg", first_20_images)


k = 100

# --8<-- [start:dict]
def construct_visual_dictionary(descriptors, k):
    """ descriptors: a list of m_i * D descriptors
        k:           int, size of the dictionary
        returns a a list where ith element is the words of the ith image
        and the kmeans object
    """
    descriptors_stack = np.vstack(descriptors)
    kmeans  = KMeans(n_clusters=k).fit(descriptors_stack)
    labels = kmeans.labels_
    image_labels = []
    row = 0
    for i, image_descriptors in enumerate(descriptors):
        image_labels.append(labels[row: row + image_descriptors.shape[0]])
        row += image_descriptors.shape[0]
    return image_labels, kmeans
# --8<-- [end:dict]
img_words, kmeans = construct_visual_dictionary(descriptors, k)

# --8<-- [start:invert]
def inverted_file_index(image_labels, k):
    """ 
        returns a list of set where ith element is the
        set of documents that has the word i
    """
    dictionary = []
    for _ in range(k):
        dictionary.append(set())
    for image, labels in enumerate(image_labels):
        for word in labels:
            dictionary[word].add(image)
    return dictionary
dictionary = inverted_file_index(img_words, k)
# --8<-- [end:invert]

# --8<-- [start:tfidf]
def compute_tfidf(img_words, k):
    """ returns a 2D image description vertor where 
        ith row is a tfidf vector t_i
    """
    N = len(img_words)
    t = np.zeros((N, k))
    for i, words in enumerate(img_words):
        for d in words:
            t[i, d] += 1
    nd = np.sum(t, axis=1)[:, None]
    ni = np.sum(t, axis=0)[None, :]
    return t / nd * np.log(N / ni)
# --8<-- [end:tfidf]
t = compute_tfidf(img_words, k)

# --8<-- [start:sim]
def sim(t, i, K):
    """ given the tfidf matrix t, find the similarity of 
        t_i against all other's and return the top K similar 
        ones
    """
    t_i = t[i][:, None]
    norms = np.linalg.norm(t, axis=1)
    sim = (t @ t_i) / ((norms * norms[i])[:, None])
    return sim.argsort(axis=0)[::-1][1:K+1].reshape(K)
# --8<-- [end:sim]

# --8<-- [start:main]
def find_candidates(kp_q, des_q, kmeans, dictionary, K):
    """ make a query given the query image, the 
        inverted file index dictionary, 
        the kmeans object, and 
        returns the top K similar image's index
    """
    k = len(kmeans.cluster_centers_)
    query_words = kmeans.predict(des_q)
    word_set = set(query_words)
    candidates = set()
    for word in word_set:
        candidates |= dictionary[word]
    candidates = list(candidates)
    cand_img_words = [query_words]
    for cand_idx in candidates:
        cand_img_words.append(img_words[cand_idx])
    tfitf = compute_tfidf(cand_img_words, k)
    similarity = sim(tfitf, 0, K)
    top_K = []
    for i in similarity:
        top_K.append(candidates[i-1])
    return top_K
# --8<-- [end:main]

def test_match(img1, img2, kp1, des1, kp2, des2):
    """ Feature Matching + Homography according to 
        https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/
        py_feature2d/py_feature_homography/py_feature_homography.html
        Input the keypoints and descriptors of the query image and the 
        test image, return the matching demo image
    """
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    return cv2.drawMatches(img1,kp1,img2,kp2,good,None)


# we make some transformation on an arbitray image in the database
# and see if we can find it back
rand_idx = np.random.randint(0, len(images))
query_image = images[rand_idx]
points2 = np.float32([[10,20], [199,10], [10,179], [180,150]])
points1 = np.float32([[0,0], [199,0], [10,199], [199,199]])
M = cv2.getPerspectiveTransform(points1, points2)
query_image = cv2.warpPerspective(query_image,M,(200, 200))



kp_q, des_q = sift.detectAndCompute(query_image, None)
db_candidates = find_candidates(kp_q, des_q, kmeans, dictionary, 6)
demo = None
for i in range(0, len(db_candidates), 2):
    cand = db_candidates[i]
    matching_col_1 = test_match(
        query_image, images[cand],
        kp_q, des_q, 
        kps[cand], descriptors[cand]
    )
    try:
        cand = db_candidates[i + 1]
        matching_col_2 = test_match(query_image, images[cand], 
                                    kp_q, des_q, 
                                    kps[cand], descriptors[cand])
    except IndexError:
        mathching_col_2 = np.zeros(query_image.shape)
    if demo is None:
        demo = np.hstack((matching_col_1, matching_col_2))
    else:
        demo = np.vstack((demo, np.hstack((matching_col_1, matching_col_2))))
cv2.imwrite("../assets/indexing_demo.jpg", demo)