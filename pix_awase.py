########## Use:
########## Last Modified:
########## Author: Yamaga
##### dependencies
from __future__ import print_function, division
import os, sys
from astropy.io import fits
import numpy as np
import astropy.io.fits
from astropy.nddata import Cutout2D
from astropy import units as u
import shutil
import optparse
import astropy


print("input")
#### input
obj = raw_input("object_name (ex. NGC7538) : ")
regrid = raw_input('IR fitsfiles  (XXX.fits,YYY.fits...) : ').split(',') # XXX.fits,YYY.fits
template2 = raw_input('regrid_template (ZZZ.fits) : ') # ZZZ.fits
print('===================================================')


waveli = []
# wavelenge search
for k in range(0,len(regrid)):
    print("search wavelen"+str(k+1)+" th start.")
    print("")

    li = []
    hdulist = astropy.io.fits.open(regrid[k])
    hdu = hdulist[0]

    data = hdu.data
    header1 = hdu.header
    try:
        a = hdu.header["WAVELEN"]
    except:
        try:
            a = hdulist[0].header["WAVELNTH"]
        except:
            print('===================================================')
            print(infile[k])
            a = input("WAVELEN = ")
            print('===================================================')
    waveli.append(a)

print('===================================================')
print("1st regrid phase")
print("")
### regrid1
fitsnames = []
template1 = regrid
for k in range(len(regrid)):
    image = '.image'
    pre = 'regrid_'

    ### CASAtasks
    importfits(fitsimage=regrid[k], imagename=regrid[k] + image)
    importfits(fitsimage=template1[k], imagename=template1[k] + image)
    imregrid(imagename=regrid[k] + image, output= pre+regrid[k]+image,template=template1[k] + image)

    print(pre+regrid[k]+image)
    exportfits(imagename=pre+regrid[k]+image, fitsimage= pre+regrid[k], overwrite=True)
    fitsnames.append(pre+regrid[k])
print("1st regrid has finished.")
print('===================================================')

print('===================================================')
print("saturate_delete phase")
print("")
### satu_delete
infile = fitsnames
fitsnames = []
wavelen = []
# wavelenge search
for k in range(0,len(infile)):
    li = []
    hdulist = astropy.io.fits.open(infile[k])
    hdu = hdulist[0]

    data = hdu.data
    header1 = hdu.header
    x = hdu.header['NAXIS1']
    y = hdu.header['NAXIS2']
    hdu.header['OBJECT'] = obj
    try:
        waveli[k] = hdu.header["WAVELEN"]
    except:
        hdu.header['WAVELEN'] = waveli[k]

    ### saturate delete
    for i in range(0,y):
        for j in range(0,x):
            v = data[i][j]
            if v == np.nan :
                v = np.nan
            elif v <= 0:
                v = np.nan
            li.append(v)

    data = np.reshape(li,[y,x]) # reshpe(x*y)

    head = astropy.io.fits.PrimaryHDU(data = data)
    head.header = header1

    filename = obj+"_"+str(waveli[k])+".fits"
    fitsnames.append(filename)
    wavelen.append(waveli[k])
    head.writeto(filename, overwrite=True)
    print("satu_delete "+str(k+1)+" th has finished.")
    print(" ")
print("wavelen : "+str(wavelen))
print("waveli : "+str(waveli))
print(fitsnames)
print("saturate_delete has finished.")
print('===================================================')

print('===================================================')
print("2nd regrid phase")
print("")
### regrid2
regrid = fitsnames
fitsnames = []
for k in range(len(regrid)):
    image = '.image'
    pre = 'regrid_'

    ### CASAtasks
    importfits(fitsimage=regrid[k], imagename=regrid[k] + image)
    importfits(fitsimage=template2, imagename=template2 + image)
    imregrid(imagename=regrid[k] + image, output= pre+regrid[k]+image,template=template2 + image)

    print(pre+regrid[k]+image)
    exportfits(imagename=pre+regrid[k]+image, fitsimage= pre+regrid[k], overwrite=True)
    fitsnames.append(pre+regrid[k])
    print(fitsnames)
print("2nd regrid has finished.")
print('===================================================')
print("FINISHED!")
### create new folder
os.mkdir(obj+"_match")
for name in fitsnames:
    shutil.move(name,obj+"_match")
