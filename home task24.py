#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.

num = int(input())
b = int(input())
c = int(input())
a = list(range(-num, (num+1)))
print(a)
mult = a[b] * a[c]
print(mult)

# mult = 0
# for i in range (-num-1, num):
#     a.append(i+1)
# print (a)
# while  (-num-1) <= b < (num+1) and (-num-1) <= c < (num+1):
#     mult = a[b] * a[c]
# print(mult)

