# Генератор персонажей, пользователю предоставлено 30 пунктов, которые
# можно распределить между четыремя характеристиками.
# необходимо, чтобы пользователь мог брать и возврашать пункты в общий
# пул, если захочет переназначить очки характеристик.
point = 30
strange = 0
intelegence = 0
heals = 0
agility = 0
choice_stat = True
stat = True
while choice_stat != "0":
    print('''1) Сила - ''', strange, '''
2) Жизнь - ''', heals, '''
3) Мудрость - ''', intelegence, '''
4) Ловкость - ''', agility, '''
Свободных очков - ''', point, '''
 
Выберете, какой пункт вы хотите изменить?
Для выхода напишите 0''')
    choice_stat = input('Только цифра: ')
    if choice_stat == '1':
        stat = strange
    elif choice_stat == '2':
        stat = heals
    elif choice_stat == '3':
        stat = intelegence
    elif choice_stat == '4':
        stat = agility
    else:
        print('Неверный ввод')
        continue
    print('''1) Добавить очки
2) Убрать очки''')
    choice = input('Введите цифру: ')
    if choice == '1':
        choice = int(input('Сколько очков добавить?: '))
        point -= choice
        stat += choice
    elif choice == '2':
        choice = int(input('Сколько очков убрать?: '))
        point += choice
        stat -= choice
    else:
        print('Неверный ввод')
