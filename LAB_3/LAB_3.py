#Развлетвляющиеся вычислительные процессы. 
#Задание2
from math import *
flag=0
print('Введите значение R ')
R=float(input('R='))
print('Введите координаты точки')
x=float(input('X='))
y=float(input('Y='))
if (x>R) or (y>R) or (x < -R) or (y < -R):
    flag=0
elif ((y<=sqrt(R**2-x**2) and (x>=0))) or ((y>=-R) \
    and (x>=-R) and (y<=x)):
    flag=1
else:
    flag=0
print("Точка X={0: 6.2F} Y={1: 6.2f}"\
    .format(x,y), end=" ")
if flag:
    print("попадает в область")
else:
    print("не попадает в область")
   