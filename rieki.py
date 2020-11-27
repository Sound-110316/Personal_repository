import numpy as np
import matplotlib.pyplot as plt

xli,Sxli = [],[]
genka,maisuu = 400,120 # 制作費用,仕入れた枚数 をいれる

while True:
    print("*-------------------------------------------------------------------*")
    x = int(input("Tシャツ一枚の価格を入れてください : "))
    print("")
    y  = -0.1*x+250
    if y > 120:
        y = 120
    Sx = x*y-genka*maisuu
    if  y == int(y):
        y = int(y)
    if  Sx == int(Sx):
        Sx = int(Sx)
    print("・販売数")
    print("    -0.1 × ["+str(x)+"] + 250 = ",y)
    print("            販売数は",y,"枚です.")
    print("")
    print("・利益")
    print("    ["+str(x)+"] × -0.1 × ["+str(x)+"] + 250 - 48000 = ",Sx)
    print("            利益は",Sx,"円です.")
    xli.append(x)
    Sxli.append(Sx)
    plt.scatter(xli,Sxli)
    plt.scatter(x,Sx)
    plt.xlabel("一枚の価格 $x$ (円)",fontname="MS Gothic")
    plt.ylabel("利益 (円)",fontname="MS Gothic")
    print("*-------------------------------------------------------------------*")
    plt.show()