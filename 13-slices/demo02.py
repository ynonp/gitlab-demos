from skimage import io
from skimage.viewer import ImageViewer

print("file 2")
#######


url = 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/5217/faces.jpg'

image = io.imread(url)
viewer = ImageViewer(image[0:400, 400:800])
viewer.show()

print(image.shape)
