#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = int(input('Input number  '))
# sumdigit = 0

# while num > 0:
#     digit = num % 10
#     sumdigit = sumdigit + digit 
#     num = num // 10

# print (sumdigit)    

num = input('Input number  ')
sum = 0

for digit in num:
    sum += int(digit)

print (sum)



