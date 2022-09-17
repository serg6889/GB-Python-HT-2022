#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#a = list("Input numbers")

# a = []
# for i in range(int(input())):
#     a.append(int(input()))
# print(a)

# a = [2, 3, 5, 9, 3]
# print(a)
# sum = 0
# for i in range(len(a)):
#     if i % 2 != 0:
#         sum+=a[i]
# print(sum)


def listsum(numlist):

    sum = 0
    for i in range(len(numlist)):
        if i % 2 != 0:
            sum+= numlist[i]
    return sum

assert(listsum([2,3,5,9,3]) == 12)
a= [2,3,5,9,3]
print(listsum(a))

# print(listsum([input('Input numbers')]))


