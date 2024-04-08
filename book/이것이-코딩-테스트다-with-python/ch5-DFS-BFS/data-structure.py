# stack
print('STACK')
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack.pop())  # 4
print(stack[-1])    # 3

print(stack[::-1])

# queue
from collections import deque
print('QUEUE')
queue = deque()
queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)

print(queue.popleft())  # 5
print(queue.pop())      # 1

# recursive function
"""
종료 조건을 꼭 명시해야 한다.
재귀 함수의 코드가 더 간결하다.

점화식을 그대로 소스코드로 옮겼다.

"""

# 2차원 리스트를 잘 이용하기만 하면, 인접행령,인접리스트 둘다 가능하다
# 인접 행렬
# graph2 = [[INF for _ in range(col)] for _ in range(row)]
# graph2 = [[INF] * col for _ in range(row)]

INF = 9999999999
col = 4
row = 3

graph2 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0],
]

for row in graph2:
    print(row)

# 인접 리스트
graph1 = [[] for _ in range(3)]

graph1[0].append((1, 7))
graph1[0].append((2, 5))

graph1[1].append((0, 7))

graph1[2].append((0, 5))

# 인접행렬과 인접리스트의 비교
"""
인접 행렬은 모든 관계를 저장하기에, 노드개수가 많을수록 메모리가 불필요하게 낭비된다.
반면에 인접리스트는 필요한 것만 저장하기에 메모리를 효율적이지만, 특정 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도는 느리다.

? 그렇다면, [{"1": 7, "2": 5}, {"0": 7,}, {"0": 5}] 이렇게 하는건 안되나?


특정한 노드와 연결된 모든 인접노드를 순회해야하는 경우 인접리스트 방식이 인접행렬방식에 비해 낭비가 적다.

"""
