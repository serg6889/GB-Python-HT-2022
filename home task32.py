#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];

# num = int(input())
# a = [ ]
# for i in range (-1, num+1):
#    a.append(i+1)
# print(a)

def func(a):
    tmp = []
    paramult = 0
    for i in range (len(a)):
        tmp.append[paramult]
        paramult+= a[i] * a[-i]
        
        return tmp

a=[0, 2, 3, 4, 5, 6]
print(a)
print(func(a))