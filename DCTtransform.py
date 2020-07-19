# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

def PSNR(original, compressed): 
    mse = np.mean((original - compressed) ** 2) 
    if(mse == 0):  # MSE is zero means no noise is present in the signal . 
                  # Therefore PSNR have no importance. 
        return 100
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse)) 
    return psnr 

image = cv2.imread('face.jpg', 1) 
cv2.imshow('Image', image)
cv2.waitKey()

image2=image/255
dct_image = cv2.dct(image2)
cv2.imshow('Dct', dct_image)
cv2.waitKey()

compressed_image = cv2.idct(dct_image)
cv2.imshow('IDCT', compressed_image)
cv2.waitKey()

value = PSNR(image, compressed_image) 
print(f"PSNR value is {value} dB") 
"""
By definition, the CR is the ratio of uncompressed data size (Suncomp) to the compressed data size (Scomp) , thus:
CR = Suncomp /  Scomp
CR is a relative measure (and dimensionless) and it is many times represented as a normalized ratio (e.g. 2:1, meaning that the uncompressed size is twice the compressed size)
bpp is an absolute measure and represents the average number of bits needed to encode each image pixel information (e.g. color).
For uncompressed image bpp is typically related to the used color model and the quantization of color information. RGB images using 8 bit per channel will give bpp = 24 bit. Gray scale images have typical bpp of 8 bit (256 levels) or 12 bit (1024 levels) depending on quantization (bit depth or color depth).
For compressed images, as they are usually transformed into different representations, the bpp is evaluated indirectly by taking the following average :  bpp = Scomp / NPixels.
So, as the number of pixels (NPixels) remains unchanged, compression ratio can be related with bpp, as follows:
CR = bppuncomp / bppcomp


bpp=8/CR

beats per pixel 

"""
