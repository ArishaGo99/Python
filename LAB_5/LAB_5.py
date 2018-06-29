#Организация циклов
#Задание2
from math import *
from random import *
flag=0
print("R           X          Y        Res") 
print("-----------------------------------")
for n in range (-5, 5):
    R=uniform(-5, 5)
    x=uniform(-5, 5)
    y=uniform(-5, 5)
    if (x<-5) or (x>5) or (x>R) or (y>R) or (y>5) or (y<-5) or (x < -R) or (y < -R):
        flag=0
    elif ((y<=sqrt(R**2-x**2) and (x>=0))) or ((y>=-R) \
    and (x>=-R) and (y<=x)):
        flag=1
    else:
        flag=0
    print("R={0: 7.2f}  X={1: 7.2f}  Y={1: 7.2f}".format(R, x, y),end=" ")
    if flag:
        print("Yes")
    else:
        print("No")
