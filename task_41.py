array = list(map(int, input("Введите массив: ").split()))
count = 0
i = 1

def search(array, i, count):
    if i >= len(array) - 1:
        return count
    if array[i - 1] < array[i] and array[i] > array[i + 1]:
        count = count + 1
    return search(array, i + 1, count)
    

print(search(array, i, count))
