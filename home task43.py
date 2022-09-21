#Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

def nonrep_l(n):
    nonrep_l = []
    for i in range (len(n+1)):
        a = int(n[i])
        if a != int(n[i+1]):
            nonrep_l.append(a)
            i+=1
    return nonrep_l

n = list(input("Input numbers \n"). split( ))   
print(n)

print(nonrep_l(n))
