def solution(s):
    answer = ''
    slen = len(s)
    if slen % 2 == 1:
        answer = s[slen//2]
    else:
        answer = s[slen//2-1:slen//2+1]
    return answer