'''import matplotlib.pyplot as plt
im = plt.imread('KA.AN2.40.jpg')
implot = plt.imshow(im)

# put a blue dot at (10, 20)
plt.scatter([ 142.9278841441], [176.53360045362])


'''
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fname = 'KA.AN2.40.jpg'
image = Image.open(fname).convert("L")
arr = np.asarray(image)
plt.imshow(arr, cmap='Greys_r')
plt.scatter([ 142.9278841441], [176.53360045362])
plt.scatter([110.06440910306], [201.20432333201])
plt.scatter([179.75120049046],[114.9064675283])
plt.scatter([145.8898005674],[113.60672314911])
plt.scatter([114.67662020506], [172.88057385995])
plt.scatter([57.811664662009],[ 160.77859813101])
plt.scatter([132.93986623677], [197.546301524])
plt.scatter([164.85603413486],[ 109.27945896467])
plt.scatter([ 87.867838541667], [131.869140625])
plt.scatter([ 129.49430581335], [126.42167684246])
plt.scatter([ 100.6875], [131.20833333333])
plt.scatter([ 112.638671875], [131.51041666667])
plt.scatter([ 170.23274739583], [126.70540364583])
plt.scatter([ 149.20726250454], [170.27109467289])
plt.scatter([91.88552596965], [113.82917496236])
plt.scatter([ 159.29166666667], [128.1875])
plt.scatter([ 146.51920572917], [129.76399739583])
plt.scatter([75.127603550727], [121.84820611412])
plt.scatter([112.31834277624], [116.14371680319])
plt.scatter([132.61118373122], [167.66661070017])
plt.scatter([157.06445001069], [197.6525322163])
plt.scatter([123.67170844479], [177.02412660478])
plt.scatter([133.43039238793], [216.80247722335])

plt.show()


