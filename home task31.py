#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#a = list("Input numbers")

a = [2, 3, 5, 9, 3]

sum = 0
for i in range(len(a)):
    if i % 2 != 0:
        sum+=a[i]
print(sum)


# def listsum(numList):

#     Sum = 0
#     for i in numList:
#         if i % 2 != 0:
#             Sum+= i
#     return Sum

# print(listsum([input('Input numbers')]))


