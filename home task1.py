#Task1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Input weekday = '))
if a == 6 or a == 7:
    print('This is Weekend !!!')
else:
    print('This is just working day')