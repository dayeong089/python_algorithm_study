# []안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화
lst = [i for i in range(0, 20) if i%2 == 1]

# 2차원 리스트를 초기화할 때는 반드시 list comprehension을 이용해야 함
n = 3
m = 4
lst = [[0] * m] * n
lst[1][1] = 5
print(lst)
# output : [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
# 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식됨(reference 복사)

n = 3
m = 4
lst = [[0] * m for _ in range(n)]
lst[1][1] = 5
print(lst)
# output : [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]
