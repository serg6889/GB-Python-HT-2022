#Напишите программу, в которой пользователь будет задавать две строки,
#а программа - определять количество вхождений одной строки в другой.
# str1 = input(' ')
# str2 = input(' ')

# numcross = 0

# for i in range(len(str1) - (len(str2)+1)):
#     if str1[i: i+ len(str2)] == str2:
#         numcross += i
# print(numcross)    
str1 = input(' ')
str2 = input(' ')

numcross = 0
current_string = str1
while True:
 if current_string.startswith(str2):
        numcross+=1
        current_string = current_string[1:]
        if len(current_string) < len(str2):
            break
print(numcross)