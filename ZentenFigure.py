############# liblaryのimport ################
import matplotlib.pyplot as plt
import aplpy as apl
import astropy.io.fits
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS

inname = r"C:\Users\yamah\Desktop\fits81656_21cm_Fix.fits" # 全天のfits
filenames = ['Fit_L134N_match\\planck_Temp_L134N_match.fits', 'Fit_NGC7538_match\\planck_Temp_NGC7538_match.fits', 'Fit_DR21_match\\planck_Temp_DR21_match.fits', 'Fit_M17_0do_match\\planck_Temp_M17_0do_match.fits', 'Fit_N7538_Fuzui_match\\planck_Temp_N7538_Fuzui_match.fits', 'Fit_Orion-KL_match\\planck_Temp_Orion-KL_match.fits', 'Fit_W28_Fuzui_match\\planck_Temp_W28_Fuzui_match.fits',"Fit_M17SW_match\planck_Temp_M17SW_match.fits","Fit_M17SWex_match\\planck_Temp_M17SWex_match.fits","Fit_Orion-B_match(3pts)\\planck_Temp_Orion-B_match.fits"] # プロットしたいfits
pre = r"C:\Users\yamah\Desktop\JUEN\seminar\Study\IR_Temp\\"
########################################## FITSの読み込み #############################################
# fig = plt.figure(figsize = (20,4)) # figが台紙のようなものでそこに画像を貼るイメージ # 図の大きさはここで決定する。
f1 = apl.FITSFigure(inname,figsize=(20,10)) # , figure=fig, subplot=(1,1,1)) # f1に作成したい図のFITSを読み込ませる

######################################## 図の作成(詳細設定) ############################################
########## glay scaleにしたい場合 ##########
# f1.show_grayscale(invert = 'set_theme',vmin =-0.05 ,vmax=1.5)  # 引数に'set_theme'で色の反転 # MAX/MINの設定はここ
########## color scaleにしたい場合 ##########
f1.show_colorscale(cmap="inferno",pmin=1,pmax=99) # 引数に何も指定しなければ、勝手に調整してくれる。(MAX/MINをとってくれる？) # カラースケールのMAX/MINの設定はここ

########## color barの設置 ##########
f1.add_colorbar() # 設置の有無
# f1.colorbar.set_location('right') # カラーバーの位置、選択肢→(right,left,top,under)
# f1.colorbar.set_width(0.2) # カラーバーの幅
# f1.colorbar.set_axis_label_text('Intensity (Jy/beam)') # カラーバーのラベルの追加

########## 軸ラベル(軸の名前)の設置 ##########
# f1.axis_labels.show() #軸ラベルあり
f1.axis_labels.hide() #軸ラベルなし
# f1.axis_labels.show_x() # X軸ラベルあり
# f1.axis_labels.hide_x() # X軸ラベルなし
# f1.axis_labels.show_y() # Y軸ラベルあり
# f1.axis_labels.hide_y() # Y軸ラベルなし
# f1.axis_labels.set_xtext('Right Ascension (J2000)') # X軸ラベルの名称の設定
# f1.axis_labels.set_ytext('Declination (J2000)') # Y軸ラベルの名称の設定

########## メモリの設置 ##########
f1.tick_labels.show() # メモリあり
# f1.tick_labels.hide() # メモリなし

########## Beamサイズの設置 ##########
# f1.add_beam() # beamサイズの有無
# f1.beam.set_frame(True) # Beamのフレームの有無
# f1.beam.set_color('black') # Beamの色
# f1.beam.set_edgecolor('black') # Beamサイズを表示するフレームの色
# f1.beam.set_facecolor('black') # フレーム内の色

########## ラベル(図内の文字)の設置 ##########
# f1.add_label(0.17, 0.95, '(a) observation', relative=True)

########## Scale barの設置 ##########
# f1.add_scalebar(0.00003) # ()でスケールを設定*この時、FITSによって単位が異なる。大体の場合は、arcsec/degree
# f1.scalebar.set_frame(True) # スケールバーを囲むフレームの有無
# f1.scalebar.set_label( '0.1" ') # スケールのラベルの設定
# f1.scalebar.set_corner('top right') # どこにスケールバーを置くかを設定

########## 図のタイトルの設定 ##########
f1.set_title('ZentenFigure') 
"""
########## 天体のプロット ############
for filename in filenames:
    filename = pre+filename
    hdu = astropy.io.fits.open(filename)[0]
    ra,dec = WCS(filename).all_pix2world((hdu.header["NAXIS1"])/2,(hdu.header["NAXIS2"])/2,0)
    gc = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='fk5').galactic
    cx, cy = gc.l.deg, gc.b.deg
    
    print(cx,cy)
    if cx > 180:
        cx = -1*(360-cx)
    f1.show_markers(cx,cy,marker="*",s=600,c="white",edgecolor="Black",lw=1)
"""
# plt.show()

plt.tight_layout()# 余白を少なく
#### Save ####
plt.savefig('zenten.png',dpi=300)
print("FINISH")