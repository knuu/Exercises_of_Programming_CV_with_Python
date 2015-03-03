from PIL import Image 
from numpy import * 
from scipy.ndimage import filters 

def self_quotient(im, sigma=5):
    """im: numpy.array gray scale image
       """
    im2 = filters.gaussian_filter(im,sigma)
    return uint8(255 * im / im2)

from pylab import *

def make_figure(im):
    figure()
    gray()
    axis('off')
    imshow(im)

def plot_im_cumsum(im, nbr_bins=256):
    """画像のヒストグラムの累積分布関数をplot
       cf. imtools.histeq"""
    imhist, _ = histogram(im.flatten(), nbr_bins, normed=True)
    plot(imhist.cumsum())

im = array(Image.open('empire.jpg').convert('L'))
make_figure(im)
make_figure(self_quotient(im))
figure()
gray()
plot_im_cumsum(im)
plot_im_cumsum(self_quotient(im))


im = array(Image.open('AquaTermi_lowcontrast.jpg').convert('L'))
make_figure(im)
make_figure(self_quotient(im))
figure()
gray()
plot_im_cumsum(im)
plot_im_cumsum(self_quotient(im))

show()
