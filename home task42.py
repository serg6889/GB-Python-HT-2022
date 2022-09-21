# Заадайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# def divider_num(n):
    
#     for i in range(2, n):
#         , while i < n**0.5]

    
#         return i

def num_multipl(n):
   i = 2
   num_multipl = []
   while i * i <= n:
       while n % i == 0:
           num_multipl.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       num_multipl.append(n)
   return num_multipl

n = int(input('Input number = \n'))  
print(num_multipl(n))
 
