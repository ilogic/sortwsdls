#!/usr/bin/python

import os

for root, dirs, files in os.walk("."):
    for file in files:
        print(root + "\\" + file)
        if (file.find("wsdl")!=-1 and file.find("sorted")==-1):
            f = open(root + "\\" + file,'r')
            w = open(root + "\\" + file+'.sorted','w')
            contenido = f.read().split('\n')
            f.close()
            contenido.sort()
            for l in contenido:
                w.write(l+'\n')
            w.close()
        
        