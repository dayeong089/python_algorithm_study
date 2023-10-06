def solution(players, callings):
    info = {key : i for i, key in enumerate(players)}
    
    for calling in callings:
        rank = info[calling]
        info[calling] -= 1
        info[players[rank-1]] += 1
        players[rank-1], players[rank] = players[rank], players[rank-1]
        
    return players