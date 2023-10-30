def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    answer = ''.join(arr)
    return answer