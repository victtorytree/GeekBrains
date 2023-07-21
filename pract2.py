# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите число монет: "))
start = int(input("Первая монета, число: 1 решка, 0 герб "))
oneSide = 0
secondSide = 0
if start == 1:
    oneSide += 1
elif start == 0:
    secondSide += 1
for i in range(1, n):
    check = int(input("монета (1/0): "))
    if check == 1:
        oneSide += 1
    if check == 0:
        secondSide += 1
if oneSide < secondSide:
    print("Перевернуть ", oneSide, "монет")
else:
    print("Перевернуть ", secondSide, "монет")

# 2
# s = int(input("Введите сумму: "))
# p = int(input("Введите произведение: "))
# d = (-1*s)**2-4*p
# x = (s - d**0.5)/2
# y = s - x
# print("Ваши числа:", x, "и", y)

# 3
# import math
# n = int(input())
# k = int(math.log(n, 2))
# i = 1
# while i <=k:
#     print(2**i)
#     i+=1





