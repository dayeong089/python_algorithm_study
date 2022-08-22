''''
퀵 정렬2
''''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    rest = lst[1:]

    left = [x for x in rest if x<=pivot]
    right = [x for x in rest if x>pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(array))
