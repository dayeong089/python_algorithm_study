def solution(arr):
    answer = []
    for x in arr:
        if answer:
            if x != answer[-1]:
                answer.append(x)
        else:
            answer.append(x)
    return answer