############# liblaryのimport ################
import numpy as np
import matplotlib.pyplot as plt
import aplpy as apl
import astropy.io.fits
from astropy.wcs import WCS
import glob


filenames1 = ['Fit_L134N_match\\planck_Temp_L134N_match.fits', 'Fit_NGC7538_match\\planck_Temp_NGC7538_match.fits', 'Fit_DR21_match\\planck_Temp_DR21_match.fits', 'Fit_M17_0do_match\\planck_Temp_M17_0do_match.fits', 'Fit_N7538_Fuzui_match\\planck_Temp_N7538_Fuzui_match.fits', 'Fit_Orion-KL_match\\planck_Temp_Orion-KL_match.fits', 'Fit_W28_Fuzui_match\\planck_Temp_W28_Fuzui_match.fits',"Fit_M17SW_match\planck_Temp_M17SW_match.fits","Fit_M17SWex_match\\planck_Temp_M17SWex_match.fits","Fit_Orion-B_match(3pts)\\planck_Temp_Orion-B_match.fits"]
for ir in range(len(filenames1)):
    if filenames1[ir] != "":
        filenames1[ir] = "IR_Temp\\"+filenames1[ir]


filenames2 = ['L134N_NH3_Temp.fits', 'N7538_NH3_Temp.fits', 'DR21_NH3_Temp.fits', 'M170do_NH3_Temp.fits', 'N7538_Fuzui_NH3_Temp.fits', 'Orion-KL_NH3_Temp.fits', 'W28_NH3_Temp.fits','M17SW_NH3_Temp.fits','M17SWex_NH3_Temp.fits',"Orion-B_NH3_Temp(nomal).fits"]
for fi in range(len(filenames2)):
    if filenames2[fi] != "":
        filenames2[fi] = "NH3_Temp\\" +filenames2[fi]

filenames = filenames1+filenames2 # 読み込むfitsを選択

regions = ["L134N.reg","NGC7538.reg","dr21-2.reg","M170d.reg","G111.reg","Ori-KL.reg","W28-TRIPCORE.reg","M17SW.reg","M17SWex.reg","IRAS1.reg"]*2 # , '', '', '', '', '', '', '','','','']
for re in range(len(regions)):
    if regions[re] != "":
        regions[re] = "reg\\" +regions[re]


vmin, vmax = [8, 14, 17, 11, 11, 18, 15, 20, 14,10]*2,[26, 33, 28, 26, 24, 50, 37, 38, 29,20]*2


fig = plt.figure(figsize=(10,50)) # figが台紙のようなものでそこに画像を貼るイメージ # 図の大きさはここで決定する。()内に"figsize = (横,縦)"を入れると図の大きさを決めれる
plt.subplots_adjust(hspace=3,wspace=3)
li = []


# plt.rcParams['font.size'] = 25 # フォントサイズの指定
for n in range(len(filenames)):

    filename=filenames[n]
    if filename != "":
        print(filename)
        ####################################### FITSの読み込み ##########################################
        if n <= 9:
            f1 = apl.FITSFigure(filename, figure=fig, subplot=(10,2,2*n+1)) # f1に作成したい図のFITSを読み込ませる
        else:
            f1 = apl.FITSFigure(filename, figure=fig, subplot=(10,2,2*(n-9))) # f1に作成したい図のFITSを読み込ませる
                                                                      # subplot(縦,横,画像の位置)
        hdu = astropy.io.fits.open(filename)[0]

        li.append(hdu)
        ######################################## 図の作成(詳細設定)############################################
        ########## glay scaleにしたい場合 ##########
        # f1.show_grayscale(invert = 'set_theme',vmin =-0.05 ,vmax=1.5)  # 引数に'set_theme'で色の反転 # MAX/MIN    の設    定はここ
        ########## color scaleにしたい場合 ##########
        f1.show_colorscale(cmap="jet",vmin=vmin[n],vmax=vmax[n]) # 引数に何も指定しなければ、勝手に調整してくれる。(MAX/MINをと    ってくれる？) # カラースケールのMAX/MINの設定はここ

        ########## color barの設置 ##########
        f1.add_colorbar() # 設置の有無
        # f1.colorbar.set_location('right') # カラーバーの位置、選択肢→(right,left,top,bottom)
        # f1.colorbar.set_width(0.2) # カラーバーの幅
        # f1.colorbar.set_axis_label_text('Intensity (Jy/beam)') # カラーバーのラベルの追加

        ########## 軸ラベル(軸の名前)の設置 ##########
        # f1.axis_labels.show() #軸ラベルあり
        # if n != 0: # 最初のグラフのみ軸ラベルを付ける
        f1.axis_labels.hide() #軸ラベルなし
        # f1.axis_labels.show_x() # X軸ラベルあり
        # f1.axis_labels.hide_x() # X軸ラベルなし
        # f1.axis_labels.show_y() # Y軸ラベルあり
        # f1.axis_labels.hide_y() # Y軸ラベルなし
        # f1.axis_labels.set_xtext('Right Ascension (J2000)') # X軸ラベルの名称の設定
        # f1.axis_labels.set_ytext('Declination (J2000)') # Y軸ラベルの名称の設定

        ########## 目盛の設置 ##########
        # f1.tick_labels.show() # 目盛あり
        f1.tick_labels.hide() # 目盛なし

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
        f1.set_nan_color(color="m") # nanの色を設定
        
        if n >= 10:
            cx,cy = WCS(filename).all_pix2world((hdu.header["NAXIS1"]-3)/2,(hdu.header["NAXIS2"]-3)/2,0) # 軸のpix数の半分をWCS座標に直して中心とする
            f1.recenter(cx,cy,radius=0.1667) # センターの設定
            f1.show_contour(li[n-10],levels=np.linspace(vmin[n],vmax[n],6),colors="k",alpha=0.7) #コントアの設定
        else:
            f1.show_contour(li[n],  levels=np.linspace(vmin[n],vmax[n],6),colors="k",alpha=0.7) # コントアの設定
            print("")
            
        
        if regions[n] != "":
            f1.show_regions(regions[n]) # regionファイルを読みこみ
        
        ########## 図のタイトルの設定 ##########
        if n < 10:
            f1.set_title(hdu.header["OBJECT"],fontsize=30)
        ########## fitsを閉じる ###########
        astropy.io.fits.open(filename).close()

fig.tight_layout()# 余白を少なく

fig.savefig("Temperature_Figure_tate.png",dpi=300)


print("FINISH")