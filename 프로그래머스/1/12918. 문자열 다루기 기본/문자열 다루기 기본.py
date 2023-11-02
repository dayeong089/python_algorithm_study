def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for ele in list(s):
        if not ele.isdigit():
            return False
    return True