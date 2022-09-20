# n = int(input('Input number N= '))

# a = [1]
# for i in range (1, n):
#     a.append(a[-1]* (-3))
# print(a)

# n = int(input('Input number '))
# num = 1
# for i in range(n):
#     print(num)
#     num *= -3

# for i in range (int(input("Input number= "))):
#     print((-3) ** i)
    
# f = open('my_file.txt', 'r')
# f_out = open('file2.txt', 'w')

# # f.writelines(['Hello!', 'ghrh', 'fdf'])
# f_out.writelines(f.readlines())

# # print(f.readlines())

# f.close()

# with open ('my_file.txt', 'r') as f:
#     # f.write('Hello!\n')
#     # f.write('dfdfdf\n')
#     # f.write('ddddd\n')
#     lines = f.readlines()
# print(1, lines)
# print(2, lines)

# a = input('Input numbers: \n').split()
# print(a)

# max_a = int(a[0])
# min_a = int(a[0])
# for i in a:
#     b = int(i)
#     if b > max_a:
#         max_a = b
#     if b < min_a:
#         min_a = b
# print(max_a, min_a)

# ax**2 + bx + c =0.  

def func_root(a, b, c):
    discr = b**2 - 4*a*c
    if discr < 0:
        x1 = ((-b) + discr**(1/2)) / (2*a)  # as complex numbers roots
        x2 = ((-b) - discr**(1/2)) / (2*a)
       # print('None of roots calculated')
        return x1, x2
    if discr == 0:
        x = (-b)/(2*a)
        return x
    elif discr > 0:
        x1 = ((-b) + discr**(1/2)) / (2*a)
        x2 = ((-b) - discr**(1/2)) / (2*a)
        return x1, x2

d= func_root(2,5,6)
print(d)






