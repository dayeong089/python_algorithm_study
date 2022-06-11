from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(1)
queue.popleft()

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue)

print(list(queue)) # deque 객체를 리스트 자료형으로 바꾸기
