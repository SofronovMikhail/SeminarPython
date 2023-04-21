arr = list(map(int, input("Введети число от 1 до 5 через пробел: ").split()))
i = len(arr)-1
def num(arr, i):
    if i == 0:
        return arr
    elif arr[i] == 5:
        arr[i] = 1
    return num(arr, i - 1)
print(num(arr, i))



