from astropy.io import fits
import os
import pandas as pd
import numpy as np

template = input("テンプレート名 : ")
hdulist = fits.open(template)
hdu = hdulist[0]
data = hdu.data
headerT = hdu.header

#input file name
input_file_name = input("ファイル名 : ") # 'planck_Temp.xlsx'
sheetNo = input("シートの番号(ex. 0) : ")
if sheetNo == "":
    sheetNo = 0
else:
    sheetNo = int(sheetNo)

#xls book Open (xls, xlsxのどちらでも可能)
input_book = pd.ExcelFile(input_file_name) 
 
#sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
input_sheet_name = input_book.sheet_names

#DataFrameとして一つ目のsheetを読込
input_sheet_df = input_book.parse(input_sheet_name[sheetNo]).iloc[::-1]
# 0をNaNで置換
input_sheet_df = input_sheet_df.replace(0,np.nan)


outfile = os.path.splitext(input_file_name)[sheetNo]


hdu = fits.PrimaryHDU(data=input_sheet_df)

# 入れたいヘッダー
hdu.header['NAXIS1'] = len(input_sheet_df.columns)
hdu.header['NAXIS2'] = len(input_sheet_df)
hdu.header["CDELT1"] = headerT["CDELT1"]*(headerT["NAXIS1"]/hdu.header['NAXIS1'])
hdu.header["CDELT2"] = headerT["CDELT2"]*(headerT["NAXIS2"]/hdu.header['NAXIS2'])
hdu.header["CRPIX1"] = (headerT["CRPIX1"]-1)*(hdu.header['NAXIS1']/headerT["NAXIS1"])+1
hdu.header["CRPIX2"] = (headerT["CRPIX2"]-1)*(hdu.header['NAXIS2']/headerT["NAXIS2"])+1
hdu.header["BLANK"]  = 0.0

# 元のfitsにあったヘッダーを入れる
headerTlist = ["BITPIX","NAXIS","EXTEND","BZERO","BSCALE","BTYPE","OBJECT","BUNIT","EQUINOX","RADESYS","LONPOLE","LATPOLE","PC1_1","PC2_1","PC1_2","PC2_2","CTYPE1","CRVAL1","CUNIT1","CTYPE2","CRVAL2","CUNIT2","LONGSTRN","EXTNAME","CLASS___","INFO____","DATA____","QTTY____","WAVELEN","DATE","TIMESYS","ORIGIN"] # "BSCALE","BZERO","BTYPE","OBJECT","BUNIT","EQUINOX","RADESYS","LONPOLE","LATPOLE","PC1_1","PC2_1","PC1_2","PC2_2","CTYPE1","CRVAL1","CRPIX1","CUNIT1","CTYPE2","CRVAL2","CRPIX1","CUNIT2"]
for h in headerTlist:
    try:
        hdu.header[h] = headerT[h]
        print(h,hdu.header[h])
    except:
        print(h,"Error")

# 作ったfitsの保存
hdu.writeto(outfile + ".fits", overwrite=True)
print("ファイル名 : [",outfile+".fits","]で保存しました！！")
