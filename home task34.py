#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#45 -> 101101

# n = int(input())
# bin = ''
# while n > 0:
#     bin = str(n % 2) + b
#     n = n // 2
# print(bin)   
 


def bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
 
n = int(input())
print(bin(n))