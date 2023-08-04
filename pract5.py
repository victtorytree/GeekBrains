#Задача 30
# a1 = int(input("Введите первый член прогрессии "))
# d = int(input("Введите разность прогрессии "))
# n = int(input("Введите кол-во членов прогрессии "))
# arif = [a1]
# for i in range(2,n+1):
#     arif.append(a1 + (i-1) * d)
# print(arif)

# Задача 32
print("Задайте список: ")
spisok = [int(input()) for i in range(1,5)]
n = int(input("Задайте минимум: "))
m = int(input("Задайте максимум: "))
sort = []
for i in spisok:
    if i >= n and i <= m:
        sort.append(i)
print(sort)
