''''
퀵 정렬
''''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(lst, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left<=right:
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        while right > start and lst[right] >= lst[pivot]:
            right -= 1

        if left > right:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:
            lst[left], lst[right] = lst[right], lst[left]

    quicksort(lst, start, right-1)
    quicksort(lst, right+1, end)

quicksort(array, 0, len(array)-1)
print(array)
