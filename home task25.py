#Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

last_position = len(list) - 1
while last_position > 1:
    random_index = random.randint(0, last_position)
    list[last_position], list[random_index] = list[random_index], list[last_position]
    last_position -= 1
   
print(list)