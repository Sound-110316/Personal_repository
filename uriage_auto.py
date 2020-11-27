import numpy as np
import matplotlib.pyplot as plt

x = 0
x_pre,Sx_pre = np.nan,np.nan
plt.figure()
plt.pause(5)
while x <= 2500:
    print("*-------------------------------------------------------------------*")
    x += 25
    print("Tシャツ一枚の価格を入れてください : ",x)
    print("")
    y  = -0.1*x+250
    Sx = x*y
    if  y == int(y):
        y = int(y)
    if  Sx == int(Sx):
        Sx = int(Sx)
    print("・販売数")
    print("    -0.1 × ["+str(x)+"] + 250 = ",y)
    print("            販売数は",y,"枚です.")
    print("")
    print("・売上額")
    print("    ["+str(x)+"] × -0.1 × ["+str(x)+"] + 250 = ",Sx)
    print("            売上額は",Sx,"円です.")
    plt.scatter(x_pre,Sx_pre,c="tab:blue")
    plt.scatter(x,Sx,c="tab:orange")
    plt.xlim(-100,4000)
    plt.ylim(-1000,175000)
    plt.xlabel("一枚の価格 $x$ (円)",fontname="MS Gothic")
    plt.ylabel("売上額 $S(x)$ (円)",fontname="MS Gothic")
    x_pre, Sx_pre = x, Sx
    print("*-------------------------------------------------------------------*")
    plt.pause(0.05)
plt.show()