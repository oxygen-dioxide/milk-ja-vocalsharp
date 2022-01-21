import os
import sys
import wavio
import numpy as np
#音频头尾各加0.2s空白

foldername=sys.argv[1]
for filename in os.listdir(foldername):
    if(filename.endswith(".wav") and not(filename.startswith("empty"))):
        print(filename)
        wav=wavio.read(os.path.join(foldername,filename))
        outputdata=np.r_[np.array([np.zeros(8820,dtype=np.int16)]).T,wav.data,np.array([np.zeros(8820,dtype=np.int16)]).T]
        #import ipdb
        #ipdb.set_trace()
        wavio.write(os.path.join(foldername,filename),outputdata,rate=44100, sampwidth=2,scale="none")
#oto转换
"""
with open(os.path.join(foldername,"oto.ini"),encoding="shift-jis") as otofile:
    lines=otofile.readlines()
otolist=[]
for line in lines:
    linecontent=line.replace("=",",").split(",")
    for i in [2,3,4,5,6]:
        linecontent[i]=float(linecontent[i])
    linecontent[2]+=200
    otolist.append(linecontent)
#import ipdb
#ipdb.set_trace()
with open(os.path.join(foldername,"oto.ini"),"w",encoding="shift-jis") as otofile:
    otofile.write("\n".join(["{}={},{},{},{},{},{}".format(*oto) for oto in otolist]))"""