#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];

# num = int(input())
# a = [ ]
# for i in range (-1, num+1):
#    a.append(i+1)
# print(a)

# def func(a):
#     tmp = []
#     paramult = 0
#     for i in range (len(a)):
#         tmp.append[paramult]
#         paramult+= a[i] * a[-i]
        
#         return tmp

# a=list(map(int, input("Input number: \n").split()))
# print(a)
# print(func(a))


def multpara(lst):
    l = len(lst)//2  
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    return (new_lst)

assert(multpara([2, 3, 4, 5, 6]) == [12, 15])
assert(multpara([2, 3, 4, 5, 6, 7]) == [14, 18, 20])

# lst = [2, 3, 4, 5, 6]
# multpara(lst)
# lst = list(map(int, input("Input number:\n").split()))
# multpara(lst)

# my_list = [2, 3, 4, 5, 6]
# result_list = []
# for i in range(len(my_list)//2):
#      result_list.append(my_list[i]*my_list[len(my_list)-1-i])
#      print(result_list)