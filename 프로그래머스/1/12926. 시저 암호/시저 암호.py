def solution(s, n):
    answer = ''
    for i in list(s):
        if i == ' ':
            answer += ' '
        else:
            now_num = ord(i)
            next_num = now_num + n
            if now_num >= ord('A') and now_num <= ord('Z'):
                if next_num > ord('Z'):
                    next_num = next_num - ord('Z') + ord('A') - 1
            elif now_num >= ord('a') and now_num <= ord('z'):
                if next_num > ord('z'):
                    next_num = next_num - ord('z') + ord('a') - 1
            answer += chr(next_num)
    return answer