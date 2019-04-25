import random 
rand_number=random.randint(1,4)
user_number=int (input('Введите число:'))

if user_number == rand_number:
    print('Победа')
elif user_number> rand_number:
    print('Загаданное число меньше')
else:
    print('Загаданное число больше')
