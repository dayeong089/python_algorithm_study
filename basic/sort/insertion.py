''''
삽입정렬
''''

# 처음 생각했던 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    now = array[i]
    for j in range(i-1, -1, -1):
        if array[j] > now:
            array[j], array[j+1] = array[j+1], array[j]
            now = array[j]
        else:
            break

print(array)

# 고친 코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)
