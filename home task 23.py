#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.
n = int(input())

a= [((1+1/i)**i) for i in range (1,n+1)]

print (a)    
sum = 0
for i in range(n+1):
    digit = a % 10
    sum = sum + digit
    a = a //10
print(round(sum,3))