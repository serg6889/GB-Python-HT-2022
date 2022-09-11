#Напишите программу, которая по заданному номеру четверти 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quaternum = int(input('Input Quater N- '))
if quaternum == 1:
    print('X => 0 and Y => 0')
elif quaternum == 2:
    print('X => 0 and Y =< 0')
elif quaternum == 3:
    print('X =< 0 and Y => 0')
elif quaternum == 4:
    print('X =< 0 and Y =< 0')