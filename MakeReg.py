import astropy.coordinates
import astropy.wcs
import astropy.io.fits
import numpy
from astropy.wcs import WCS
import glob

filenames = glob.glob("./fits/*") # input("filenames : ").split(",")

for filename in filenames:
    fits = astropy.io.fits.open(filename)
    header = fits[0].header
    data = fits[0].data

    w = WCS(filename)
    nax1,nax2 = header["NAXIS1"],header["NAXIS2"]
    # header["CRPIX"]
    galx, galy = w.all_pix2world((nax1-3)/2, (nax2-3)/2, 0) #pix座標から世界座標に変換
    print(header["OBJECT"],galx,galy)
    # 銀河座標で作成
    coord = astropy.coordinates.SkyCoord(galx, galy, frame='galactic', unit='deg')
    center = coord.to_string('hmsdms').replace("h",":").replace("d",":").replace("m",":").replace("s","").replace(" ",",")

    width,height = abs(nax1*header["CDELT1"]*3600),abs(nax2*header["CDELT2"]*3600)


    path_w = "reg\\"+header["OBJECT"]+'.reg'
    s = '# Region file format: DS9 version 4.1\nglobal color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\nfk5\nbox('+center+","+str(width)+"\","+str(height)+'\",0) # color=black width=2'

    with open(path_w, mode='w') as f:
        f.write(s)
print("FINISH")
