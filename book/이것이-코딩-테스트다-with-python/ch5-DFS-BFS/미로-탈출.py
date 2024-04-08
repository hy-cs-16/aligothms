from collections import deque

DIR_X = [-1, 1, 0, 0]
DIR_Y = [0, 0, -1, 1]
MOVE_TYPES_COUNTS = 4


def solution(maze):
    # 인접그래프가 존재한 상황에서, visited 를 따로 관리해야할까?
    return bfs2(maze, (0, 0))

class Coord:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value

    def __str__(self):
        return f'({self.i}, {self.j}) depth : {self.value}'


def bfs(maze, start):
    n = len(maze)
    m = len(maze[0])

    visited = [[c == 0 for c in row] for row in maze]

    i, j = start
    q = deque([Coord(i, j, 1)])
    visited[i][j] = True
    max_depth = None

    while len(q) != 0:
        top = q.popleft()
        print(top)
        for row in visited:
            for v in row:
                text = '*' if v else '-'
                print(text, end='')
            print()

        max_depth = top.value

        if top.i == n - 1 and top.j == m - 1:
            break

        for t in range(MOVE_TYPES_COUNTS):
            ni = top.i + DIR_X[t]
            nj = top.j + DIR_Y[t]

            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1 and visited[ni][nj] is False:
                q.append(Coord(ni, nj, top.value + 1))
                visited[ni][nj] = True

    return max_depth


def bfs2(maze, start):
    n = len(maze)
    m = len(maze[0])

    i, j = start
    q = deque([Coord(i, j, 1)])
    maze[i][j] = 0
    max_depth = None

    while len(q) != 0:
        top = q.popleft()
        max_depth = top.value

        if top.i == n - 1 and top.j == m - 1:
            break

        for t in range(MOVE_TYPES_COUNTS):
            ni = top.i + DIR_X[t]
            nj = top.j + DIR_Y[t]

            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1:
                q.append(Coord(ni, nj, top.value + 1))
                maze[ni][nj] = 0

    return max_depth


test_case_1 = [
 [1, 0, 1, 0, 1, 0],
 [1, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]
]

print(solution(test_case_1))

def solution_in_book():
    pass