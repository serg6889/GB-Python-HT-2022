#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#a = list("Input numbers")

# a = []

# a.append(n)
# sum = 0
# for i in range(n):
#     if i % 2 !== 0:
#         sum+=i
# print(sum)

def listsum(numList):

    Sum = 0
    for i in numList:
        if i % 2 != 0:
            Sum+= i
    return Sum

print(listsum([input('Input numbers')]))
