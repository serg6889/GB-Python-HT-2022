#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Input N= '))
# a= []
# for i in range (n+1):
#    a.append(i+1)
# print (a)    

n = int(input())
mult = 1

for i in range (1, n+1):
   mult *= i
print (mult) 