def solution(name, yearning, photo):
    answer = [0 for _ in range(len(photo))]
    score = {}
    for i, p in enumerate(name):
        score[p] = yearning[i]
        
    for i, ps in enumerate(photo):
        for p in ps:
            if p in score.keys():
                answer[i] += score[p]
                
    return answer