from PIL import Image 
from numpy import * 
from scipy.ndimage import filters 

def unsharp_masking(im, sigma=5):
    """im: numpy.array image
       cf. 1.4.1.gauss.py"""
    im2 = filters.gaussian_filter(im,sigma)
    return im2 - im

def unsharp_masking_color(im, sigma=5):
    """im: numpy.array image
       cf. 1.4.1.gauss_color.py"""
    im2 = zeros(im.shape) 
    for i in range(3):
        im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
    im2 = uint8(im2)
    return im2 - im

from pylab import *

def make_figure(im):
    figure()
    gray()
    axis('off')
    imshow(im)

im = array(Image.open('empire.jpg').convert('L'))
make_figure(im)
make_figure(unsharp_masking(im))

im = array(Image.open('empire.jpg'))
make_figure(im)
make_figure(unsharp_masking_color(im))

show()
