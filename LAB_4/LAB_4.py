#Организация циклов. 
#Задание1
from math import *
print('Введите Xbeg, Xend и Dx')
xb=float(input('Xbeg='))
xe=float(input('Xend='))
dx=float(input('Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("  Dx={0: 7.2f}".format(dx))
xt=xb
print("+--------+--------+")
print("I   X    I    Y   I")  
print("+--------+--------+")
while xt<=xe:
    if xt<0:
            y=-(0.5)*xt - 3
            print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    elif xt>=0 and xt<3:
            y=-sqrt(9-xt**2)
            print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    elif xt>=3 and xt<=6:
            y=sqrt((xt+9)*(xt+3))
            print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt+=dx
print("+--------+--------+")   
