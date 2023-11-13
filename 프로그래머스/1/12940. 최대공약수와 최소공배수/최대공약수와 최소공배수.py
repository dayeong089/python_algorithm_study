def solution(n, m):
    answer = []
    min_value = min(n, m)
    for i in range(min_value, 0, -1):
        if n%i==0 and m%i==0:
            answer.append(i)
            answer.append(i * (n//i) * (m//i))
            break
    return answer