# n = int(input("n: "))
# m = int(input("m: "))
# print("Введите элементы первого множества: ")
# spisok1 = [int(input()) for i in range(n)]
# print("Введите элементы второго множества: ")
# spisok2 = [int(input()) for i in range(m)]
# set1 = set(spisok1)
# set2 = set(spisok2)
# res = set1.intersection(set2)
# print(*spisok1)
# print(*spisok2)
# if len(res) >= 1:
#     print(*res)
# else: 
#     print("Введены массивы без повторяющихся данных")

# №24 - про ягоды
bar = [1, 4, 5, 7, 1]
N = len(bar)
maxHeld = 0
for i in range(N):
    if i == N-1:
        summa = bar[i-1]+bar[i]+bar[0]
    else:
        summa = bar[i-1]+bar[i]+bar[i+1]
    if summa > maxHeld:
        maxHeld = summa
        maxIndex = i
print(maxHeld, "куст:", maxIndex+1)