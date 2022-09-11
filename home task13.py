# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Input X = '))
y = int(input('Input Y = '))
if x > 0 and y > 0:
    print('Quater N-1')
elif x > 0 and y < 0:
    print('Quater N-2')
elif x < 0 and y < 0:
    print('Quater N-3')
elif x < 0 and y > 0:
    print('Quater N-4')