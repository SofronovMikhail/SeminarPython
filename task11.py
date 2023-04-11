
num = int(input("Введите число: "))
limit = 30
i = 2
sum = limit * [0]
while i <= limit:
    sum[0] = 0
    sum[1] = 1
    sum[i] = sum[i - 1] + sum[i - 2]
    if (sum[i] == num):
        print(i)
        break
    i = i + 1

