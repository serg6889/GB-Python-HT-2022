#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = abs(int(input('Input number  ')))
# sumdigit = 0

# while num > 0:
#     digit = num % 10
#     sumdigit = sumdigit + digit 
#     num = num // 10

# print ('Sum of digits =',  sumdigit)    


num = input('Input float number  ')
sum = 0

for digit in num:
    if digit != '.':
        sum += int(digit)

print (sum)



