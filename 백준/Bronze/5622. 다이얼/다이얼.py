x = input()
total_time = 0
for i in range(len(x)):
    time = 2
    now = ord(x[i])
    if now>=65 and now<=67: #ABC
        time += 1
    elif now>=68 and now<=70: #DEF
        time += 2
    elif now>=71 and now<=73: #GHI
        time += 3
    elif now>=74 and now<=76: #JKL
        time += 4
    elif now>=77 and now<=79: #MNO
        time += 5
    elif now>=80 and now<=83: #PQRS
        time += 6
    elif now>=84 and now<=86: #TUV
        time += 7
    elif now>=87 and now<=90: #WXYZ
        time += 8
    total_time += time
    
    
print(total_time)
