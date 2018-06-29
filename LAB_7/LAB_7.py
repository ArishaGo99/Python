#Двумерные массивы и функции
from random import *
from functools import reduce
from operator import mul
n=int(input("Введите размер матрицы (NxN): "))
A=[] 
for i in range(n):
    A.append([0]*n)
for Row in range(n): 
    for Col in range(n): 
        A[Row][Col]=randint(-5,5) 
for Row in range(n): 
    for Col in range(n):
        print("{0:2}".format(A[Row][Col]), end=" ")
    print()
print()
#Нахождение произведения элементов в тех строках, которые не содержат отрицательных элементов
for Row in range (n):
    p=1
    for Col in range (n):
        if A[Row][Col]>0:
            p=p*A[Row][Col]
        else:
            p=1
            break
if p==1:
    print ("Таких строк нет")
else:
    print(p)
#Нахожждение максимума среди сумм элементов диагоналей, параллельных главной диагонали матрицы






    





