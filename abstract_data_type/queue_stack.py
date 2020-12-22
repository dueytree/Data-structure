# deque 는 파이썬 collections 모듈에서 가지고 온다

## queue
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue)   # 큐 출력

# 큐의 가장 앞 데이터 접근
print(queue[0])

# 큐 맨 앞 데이터 삭제
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)

## stack
from collections import deque

stack = deque()
# stack 은 리스트와 deque 사용방법이 똑같다.
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)   # 스택 출력
# 맨 끝 데이터 접근
print(stack[-1])
# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)   # 스택 출력