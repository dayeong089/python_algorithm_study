def recursion(i):
    print(str(i) + "번째 함수")

    if i==100: # 종료조건
        return
    recursion(i+1)

recursion(1)
