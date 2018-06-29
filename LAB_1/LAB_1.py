#Линейные программы
import math

import sys, traceback

while True:
    try:
       a=""
       a=input ('Введите параметр a в градусах: ')
       a=int(a)
       break
    except ValueError:
        if a=="":
             a=0
        print('Неверно. Повторите ввод еще раз. a-int. Пример: 100.')
if (a==90) or (a==270):
   print ("В данных областях tg не существует")
elif a>=360:
     a=a-360
if (a==90) or (a==270):
    print ("В данных областях tg не существует")
if (a==30) or (a==150) or (a==210) or (a==330): 
    print ("0")
elif a>=360:
     a=a-360
if (a==30) or (a==150) or (a==210) or (a==330):
    print ("0")
if (a==60) or (a==120) or (a==240) or (a==300):
    print ("0")
elif a>=360:
     a=a-360
if (a==60) or (a==120) or (a==240) or (a==300):
    print ("0")
else:
     z1=(2*round ((math.cos(math.radians(a)))*round ((math.sin(math.radians(2*a))))) - 
        round ((math.sin(math.radians(a))))) / (round((math.cos(math.radians(a)))) -
        (2*round((math.sin(math.radians(a))))*(math.sin(math.radians(2*a)))))
     print("z1={0:.3f}". format (z1))  
     z2=round ((math.tan(math.radians(3*a))))
     print("z2={0:.3f}". format (z2)) 

    
    
       
      
   
     
           
  








