import astropy.io.fits
import numpy as np

inname = input("filename(fullpath) : ")
fits = astropy.io.fits.open(inname)
hdu = fits[0]
header = hdu.header
header["CDELT3"] = 1

hdu.writeto(inname[:-4]+"_Fix.fits",overwrite=True)