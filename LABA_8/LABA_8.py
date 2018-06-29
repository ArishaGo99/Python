
# Компьютер выбирает какое-либо слово, а игрок должен его отгадать. Компьютер сообщает игроку, 
# сколько букв в слове, и даёт 5 попыток узнать, если ли какая-либо буква в слове, причем
# программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово
import random
 
WORDS = ("питон", "программист", "вирус", "сервер")
word = random.choice(WORDS)
correct = word
print("""Добро пожаловать в игру "Угадай слово"! 
Компьютер загадывает слово и Вам нужно его угадать. 
У Вас есть 5 попыток узнать, есть ли какая-то буква
в слове, после чего нужно попытаться угадать слово. Удачи!""")
print("Загаданное слово содержит {} букв.".format(len(correct)))
counter = 1
while True:
    if counter <= 5:
        letter = input("\nВведите букву: ")
        if letter.isalpha() and len(letter) == 1:
            if letter in correct:
                print("Да, такая буква есть в слове.")
                counter += 1
            else:
                print("Нет, такой буквы нет в слове.")
                counter += 1
        else:
            print("Возможно, Вы ввели не букву.")
            
    else:
        counter = 1
        break
while True:
    if counter <= 5:
        guess = input("\nТеперь постарайтесь угадать слово: ")
        if not guess.isalpha():
            print("Возможно, Вы не ввели слово.")
        elif guess != correct:
            print("Попробуйте еще раз. Количество оставшихся попыток: {}".format(5 - counter))
            counter += 1
        elif guess == correct:
            print("Вы угадали слово!")
            break
    else:
        print("Вы проиграли.")
        break
 
input("\n\nНажмите Enter для выхода.")