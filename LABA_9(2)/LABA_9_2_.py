import random
MENU =  (
    """
    0 - Выход
    1 - Посмотреть текущие характеристики
    2 - Изменить Сила
    3 - Изменить "Здоровье"
    4 - Изменить "Ловкость"
    5 - Изменить "Мудрость"
    """
    )
MENU_ABILITY = (
    """
    0 - Выход в предыдущее меню
    1 - Добавить очки
    2 - Удалить очки
    """
    )
points = 30
add_points = 0
del_points = 0
abilities = {"Сила": 0, "Здоровье": 0, "Ловкость": 0, "Мудрость": 0}
choice = None
while choice != "0":
    choice2 = None
    print(MENU)
    choice = input("Ваш выбор: ")
    print()
    # выход
    if choice == "0":
        print ("До свидания")
    #просмотр текущих характеристик
    elif choice == "1":
        print("Количество свободных очков:", points, "\nТекущие характеристики:", abilities)
    #изменить ветку Сила
    elif choice == "2":
        while choice2 != "0":
            print("\nУ вас есть", points, "свободных очков и", abilities["Сила"], "очков в ветке Сила.")
            print (MENU_ABILITY)
            choice2 = input("Ваш выбор: ")
            print()
            if choice2 == "0":
                print ("Возврат к предыдущему меню")
            elif choice2 == "1" and points > 0:
                add_points = int(input("Сколько очков хотите добавить в ветку Сила?\n"))
                if add_points > points:
                    print ("\nВы хотите добавить больше очков, чем есть у вас на самом деле.")
                elif add_points <= points:
                    points -= add_points
                    abilities["Сила"] += add_points
            elif choice2 == "2" and abilities["Сила"] > 0:
                del_points = int(input("Сколько очков хотите убрать из ветки Сила?\n"))
                if del_points > abilities["Сила"]:
                    print ("\nВы хотите убрать больше очков, чем есть в ветке Сила.")
                elif del_points <= abilities["Сила"]:
                    points += del_points
                    abilities["Сила"] -= del_points
            elif (choice2 == "1" and points == 0):
                print("Нет свободных очков")
            elif (choice2 == "2" and abilities["Сила"] == 0):
                print("В ветке Power нет очков")
            else:
                print("Неправильный ввод")
                
    #изменить ветку Здоровье
    elif choice == "3":
        while choice2 != "0":
            print("\nУ вас есть", points, "свободных очков и", abilities["Здоровье"], "очков в ветке Здоровье.")
            print (MENU_ABILITY)
            choice2 = input("Ваш выбор: ")
            print()
            if choice2 == "0":
                print ("Возврат к предыдущему меню")
            elif choice2 == "1" and points > 0:
                add_points = int(input("Сколько очков хотите добавить в ветку Здоровье?\n"))
                if add_points > points:
                    print ("\nВы хотите добавить больше очков, чем есть у вас на самом деле.")
                elif add_points <= points:
                    points -= add_points
                    abilities["Здоровье"] += add_points
            elif choice2 == "2" and abilities["Здоровье"] > 0:
                del_points = int(input("Сколько очков хотите убрать из ветки Здоровье?\n"))
                if del_points > abilities["Health"]:
                    print ("\nВы хотите убрать больше очков, чем есть в ветке Health.")
                elif del_points <= abilities["Здоровье"]:
                    points += del_points
                    abilities["Здоровье"] -= del_points
            elif (choice2 == "1" and points == 0):
                print("Нет свободных очков")
            elif (choice2 == "2" and abilities["Здоровье"] == 0):
                print ("В ветке Health нет очков")
            else:
                print("~~Неправильный ввод~~")
                
    #изменить ветку Ловкость
    elif choice == "4":
        while choice2 != "0":
            print("\nУ вас есть", points, "свободных очков и", abilities["Ловкость"], "очков в ветке Ловкость.")
            print (MENU_ABILITY)
            choice2 = input("Ваш выбор: ")
            print()
            if choice2 == "0":
                print ("Возврат к предыдущему меню")
            elif choice2 == "1" and points > 0:
                add_points = int(input("Сколько очков хотите добавить в ветку Ловкость?\n"))
                if add_points > points:
                    print ("\nВы хотите добавить больше очков, чем есть у вас на самом деле.")
                elif add_points <= points:
                    points -= add_points
                    abilities["Ловкость"] += add_points
            elif choice2 == "2" and abilities["Ловкость"] > 0:
                del_points = int(input("Сколько очков хотите убрать из ветки Ловкость?\n"))
                if del_points > abilities["Agility"]:
                    print ("\nВы хотите убрать больше очков, чем есть в ветке Ловкость.")
                elif del_points <= abilities["Ловкость"]:
                    points += del_points
                    abilities["Ловкость"] -= del_points
            elif (choice2 == "1" and points == 0):
                print("Нет свободных очков")
            elif (choice2 == "2" and abilities["Ловкость"] == 0):
                print ("В ветке Ловкость нет очков")
            else:
                print("Неправильный ввод")
    #изменить ветку Мудрость
    elif choice == "5":
        while choice2 != "0":
            print("\nУ вас есть", points, "свободных очков и", abilities["Мудрость"], "очков в ветке Мудрость.")
            print (MENU_ABILITY)
            choice2 = input("Ваш выбор: ")
            print()
            if choice2 == "0":
                print ("Возврат к предыдущему меню")
            elif choice2 == "1" and points > 0:
                add_points = int(input("Сколько очков хотите добавить в ветку Мудрость?\n"))
                if add_points > points:
                    print ("\nВы хотите добавить больше очков, чем есть у вас на самом деле.")
                elif add_points <= points:
                    points -= add_points
                    abilities["Мудрость"] += add_points
            elif choice2 == "2" and abilities["Мудрость"] > 0:
                del_points = int(input("Сколько очков хотите убрать из ветки Мудрость?\n"))
                if del_points > abilities["Мудрость"]:
                    print ("\nВы хотите убрать больше очков, чем есть в ветке Мудрость.")
                elif del_points <= abilities["Мудрость"]:
                    points += del_points
                    abilities["Мудрость"] -= del_points
            elif (choice2 == "1" and points == 0):
                print("Нет свободных очков")
            elif (choice2 == "2" and abilities["Мудрость"] == 0):
                print ("В ветке Wisdom нет очков")
            else:
                print("Неправильный ввод")
