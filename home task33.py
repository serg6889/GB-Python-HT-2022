#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

#def funcmax(n):

#     for i in range(len(n)):
        
#         if (n(i) % 1) > (n(i+1) % 1):
#             (n(i) % 1) == max
#             max+=i
#     return max

#     def funcmin(n):

#         for i in range(len(n)):


# n = [1.1, 1.2, 3.1, 5, 10.01]


n = list(map(float, input("Input number: \n").split()))
a = [round(i%1, 3) for i in n]
print(max(a) - min(a))