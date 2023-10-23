def solution(arr):
    min_value = min(arr)
    arr.remove(min_value)
    if len(arr) == 0:
        arr.append(-1)
    return arr