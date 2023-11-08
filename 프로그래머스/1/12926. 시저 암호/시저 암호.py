def solution(s, n):
    answer = ''
    for i in list(s):
        if i == ' ':
            answer += ' '
        else:
            now_num = ord(i)
            next_num = now_num + n
            if i.isupper():
                if next_num > ord('Z'):
                    next_num = next_num - ord('Z') + ord('A') - 1
            elif i.islower():
                if next_num > ord('z'):
                    next_num = next_num - ord('z') + ord('a') - 1
            answer += chr(next_num)
    return answer