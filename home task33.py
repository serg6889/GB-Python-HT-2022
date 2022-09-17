#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_max_min(n):
    max = n[0]
    min = n[0]
    for i in n[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    return (min, max)

def find_diff(n):

    a = [round(i%1, 3) for i in n if i%1 != 0]

    (min, max)=find_max_min(a)
    print(min, max)
    return (max - min)


n = [1.1, 1.2, 3.1, 5, 10.01]
print(find_diff(n))    
assert(find_diff(n) == 0.19)
           
        


# n = list(map(float, input("Input number: \n").split()))
# a = [round(i%1, 3) for i in n]
# print(max(a) - min(a))