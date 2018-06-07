from skimage import io
from skimage.viewer import ImageViewer
import numpy as np

image = io.imread('https://s3-us-west-2.amazonaws.com/s.cdpn.io/5217/faces.jpg')

image[image[:,:,0] > 160] += np.array([0, 60, 0], dtype='uint8')

v = ImageViewer(image)
v.show()
