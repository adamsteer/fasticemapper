# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 10:48:25 2015

@author: adam
"""
#import some packages.. 
from PIL import Image
import glob
import numpy as np

dates = '061-075'

#get a list of candidate images
imgList = glob.glob('./raw_tiff/*'+ dates + '_foradam.tif')
first = True

print imgList

#loop through images...
for img in imgList:
    temp = np.asarray(Image.open(img))
    temp = temp.astype('float')
    if first:
        #create the blank image
        
        first = False
        fastIce = np.where(temp == 1,temp,0)
        sumImage = fastIce
        
    else:
        
        #what do we want here... how many times a pixel is assigned a value..
        #essentially a histogram of pixel values through the image stack
        #..which is made easy because fast ice = 1...
        #1. get pixel indices for fast ice
        fastIce = np.where(temp == 1,temp,0)
        #2. add the fast ice pixels to the sumImage.
        sumImage = sumImage + fastIce

#avgArray = sumImage/len(imgList)

pdfArray = sumImage/(len(imgList)-1)
#pdfArray = sumImage
pdfArray = np.nan_to_num(pdfArray)

pdfImg = Image.fromarray(pdfArray)

#pdfImg = Image.fromarray(pdfArray.astype('uint8'))
#pdfImg.show()
pdfImg.save('./fortnight_pdfs/fastice_'+dates+'_pdf.tif')

print('done')