#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Input N= '))
# a= []
# for i in range (n+1):
#    a.append(i+1)
# print (a)    

n = int(input('Input N= '))
a= 1
for i in range (2, n+1):
   a *= i
print (a) 