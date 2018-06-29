#Одномерные массивы
from math import *
from random import *
import numpy as np 
n = int(input("Элементов в массиве (N<=30) N: "))
#Генерация массива и вывод
print("Начальное состояние")
mas = []
for i in range(n):
    mas.append(uniform(-5, 5))
    print("{0: 7.3f}".format(mas[i]), end=" ")
print()
#Нахождение суммы элементов с нечетными номерами
asum=0.0
for i in range (n):
    if i%2!=0.0:
        asum+=mas[i]   
#Нахождение суммы между превым и последним отрицательным элементом
min1=0
min2=0
for i in range (n): 
    if mas[i]<0:
       min1=i
       break
mas.reverse()
for i in range (n):
    if mas[i]<0:
       min2=n-i-1
       break
mas.reverse()
sum=0.0
for i in range (min1, min2):
    if min1!=min2:
        sum=sum+mas[i]    
    elif min2-min1==1:
         print("0")
    else:
         print("0")
#Сортировка массива
j=0
for i in range (n):
    if abs(mas[i])>=1:
        mas[j]=mas[i]
        j=j+1        
for i in range (j, n):
    mas[i]=0.0
#Массив после сортировки
print ("Конечное состояние")
for i in range (n):
    print ("{0: 7.3f}".format(mas[i]), end=" ")
print() 
print("Cумма элементов с нечетными номерами={0: 7.3f}".format(asum))
print("Сумма между первым и последними отрицательными элементами={0: 7.3f}".format(sum))
    





        




   
       
    



        




       