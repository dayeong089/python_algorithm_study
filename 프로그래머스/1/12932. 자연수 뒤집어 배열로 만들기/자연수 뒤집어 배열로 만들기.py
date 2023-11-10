def solution(n):
    # return list(map(int, list(str(n))))[::-1]
    return [int(i) for i in list(str(n))][::-1]