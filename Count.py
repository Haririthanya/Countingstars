
# coding: utf-8

# In[1]:

#import libraries
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread


# In[14]:
#import the picture and convert it to grayscale image and plot the image

example_file = glob.glob(r"C:/Users/Lenovo/Desktop/sky2.jpg")[0]
im = imread(example_file, as_grey=True)
cm_gray = plt.get_cmap('gray')
plt.imshow(im, cmap=cm_gray)
plt.show()


# In[15]:

#To detect objects .Blobs_log gives three outputs for each object found. First two are the coordinates and the third one is the area of the object. The radius of each blob/object can be estimated using this column (area of the object). 
blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : " ,numrows)


# In[16]:

# To validate whether we captured all stars
fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=cm_gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)

