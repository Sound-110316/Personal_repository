import glob
import os
import subprocess
import shutil

import time
start = time.time()

ext = ".md"  # 表示したい拡張子
os.chdir("./") # 拡張子を探したいディレクトリのパス
css = r"./markdown.css" # cssのパス


def Extend(x): # ディレクトリの下に指定の拡張子があるか調べる
    global Ex
    f = glob.glob(x+"/*")
    for j in f:
        if ext in j:
            Ex = True
        elif os.path.isdir(j):
             Extend(j)

def md(x):
    global Ex
    files = sorted(glob.glob(x), key=lambda f: os.stat(f).st_mtime, reverse=True)
    for file in files:
        if os.path.isdir(file):
            listpath = file.split("\\")
            space = "- "
            for s in range(len(listpath)-2):
                space = "    "+space
            fili = sorted(glob.glob(file+"/*"+ext), key=lambda f: os.stat(f).st_mtime, reverse=True)
            if (fili != []) and (ext == ".md"):
                shutil.copyfile(css,file+"/markdown.css")
            Ex = False
            Extend(file)
            if Ex:
                op.write(space+"**["+listpath[-1]+"]**\n")
            for n in fili:
                filename=glob.glob(os.path.splitext(n)[0]+"*")
                for o in filename:
                    op.write("    "+space+"["+os.path.basename(o)+"]"+"("+o[2:]+")"+"\n")
            md(file+"/*")


op = open("./Tree.md",mode="w",encoding='UTF-8')
op.write("## File and Folder Tree\n")
md("./*")
op.close()
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
subprocess.run('Tree.md', shell=True)