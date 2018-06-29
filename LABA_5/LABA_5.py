import random 
print ('Давайте поиграем! Вам необходимо отгадать один из цветов светофора')
inventory = ["красный", "желтый", "зеленый"]
print ("\n")
color = input ("Введите название цвета: ")
random_inventory = random.choice (inventory)
print (random_inventory)
input ("\n\n Нажмите Enter для продолжения")
print ("\n")
