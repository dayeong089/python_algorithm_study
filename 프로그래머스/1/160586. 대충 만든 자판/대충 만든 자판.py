def solution(keymap, targets):
    answer = [0] * len(targets)
    for idx, target in enumerate(targets):
        for target_char in target:
            min_count = 101
            for key in keymap:
                now_cnt = key.find(target_char)
                if now_cnt != -1 and now_cnt < min_count:
                    min_count = now_cnt + 1
            if min_count == 101:
                answer[idx] = -1
                break
            answer[idx] += min_count
    return answer