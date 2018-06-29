import random 
print ('Давайте поиграем! Вам необходимо отгадать один из цветов светофора. Чем меньше попыток вы используете, тем больше очков наберете. У вас есть 3 попытки')
inventory = ["красный", "желтый", "зеленый"]
print ("\n")

random_inventory = random.choice (inventory)

a = 3
bal = 15
while a > 0:
    
    color = input ("Введите название цвета: ")
    if random_inventory == color:
        print ("ВЕРНО!", bal)
        break
    else:
        print ("НЕВЕРНО!")
        if a > 0:
            print ("Попробуйте снова. У вас осталось", a, "попытки")

        else:
            print ("Правильный ответ: ", random_inventory)
    a = a - 1
    bal = bal - 5
       
input ("\n\n Нажмите Enter для продолжения")
print ("\n")

