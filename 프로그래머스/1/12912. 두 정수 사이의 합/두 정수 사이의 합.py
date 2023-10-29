def solution(a, b):
    arr = [x for x in range(min(a,b), max(a,b)+1)]
    return sum(arr)