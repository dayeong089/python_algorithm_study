def solution(s):    
    p_num = s.count('p') + s.count('P')
    y_num = s.count('y') + s.count('Y')

    return p_num == y_num