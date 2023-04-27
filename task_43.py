array = list(map(int, input("Введите массив: ").split()))
count = 0

def search(count):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count = count + 1
    return count

print(search(count))