import random

WORDS = ("питон", "пермешать", "легко", "сложно", "ответ", "ксилофон", "атака", "условие", 
         "беседовать", "вселенная")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Добро пожаловать в игру 'Анаграммы'! Надо переставить буквы так, чтобы получилось осмысленное слово")
print("Вот анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
hint=''
x=0
score=0

while guess != correct:
    print("К сожалению, вы не правы")
    hint = input('Если Вам нужна подсказка, нажмите да либо Enter' )
    if hint.lower()=="да":
          x=random.randrange(len(correct))
          print(" {} буква {}".format(x, correct[x]))
          score-=1
    else:
        score+=1
    guess = input("Попробуйте отгадать исходное слово: ")
   
   
if guess == correct:
    print("Правильно! Вы отгадали!\n")
    score+=1
    print("Ваш счет ", score)

print("Спасибо за игру")

input("\n\nНажмите Enter для выхода")