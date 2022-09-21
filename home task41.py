#Вычислить число π c заданной точностью d
#*Пример:* - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = int(input('Input requested precision of Pi = \n'))
k = 1

s = 0
 
for i in range(d):
    if i % 2 == 0:
        s += 4/k
    else:
        s -= 4/k
 
    k += 2
     
print(s)