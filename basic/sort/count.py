''''
계수 정렬
''''

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

min_value = min(array)
max_value = max(array)

length = max(array) - min(array) + 1
lst = [0] * length

for x in array:
    lst[x-min_value] += 1

for i in range(len(lst)):
    for _ in range(lst[i]):
        print(i+min_value, end=' ')
