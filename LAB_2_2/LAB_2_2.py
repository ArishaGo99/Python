#Развлетвляющиеся вычислительные процессы. 
#Задание1.Вариант листинга №2
from math import *
x=float(input('Введите значение x= '))
if x<0:
    y=-(0.5)*x-3
    print("X={0:.2f} Y{1:.2F}".format(x,y))
elif x>=0 and x<3:
    y=-sqrt(9-x**2)
    print("X={0:.2f} Y{1:.2F}".format(x,y))
elif x>=3 and x<6:
     y=sqrt((x+9)*(x+3))
     print("X={0:.2f} Y{1:.2F}".format(x,y))
else:
    print('Не принадлежит графику')
