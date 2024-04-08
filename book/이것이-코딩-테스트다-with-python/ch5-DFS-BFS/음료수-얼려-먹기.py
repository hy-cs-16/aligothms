ICE = 0
BLOCK = 1

DIR_X = [-1, 1, 0, 0]
DIR_Y = [0, 0, -1, 1]
MOVE_TYPES_COUNT = 4

test_case_1 = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]


def solution(ice_box):
    visited = [[coord == BLOCK for coord in row] for row in ice_box]

    ice_list = []

    for i  in range(len(ice_box)):
        for j in range(len(ice_box[0])):
            if ice_box[i][j] == ICE:
                ice_list.append((i, j))

    count = 0
    for coord in ice_list:
        x = coord[0]
        y = coord[1]

        if not visited[x][y]:
            dfs(ice_box, coord, visited)
            count += 1

    return count


def dfs(ice_box, coord, visited):
    x = coord[0]
    y = coord[1]

    visited[x][y] = True

    for i in range(MOVE_TYPES_COUNT):
        dx = DIR_X[i]
        dy = DIR_Y[i]

        nx = x + dx
        ny = y + dy

        if 0 <= nx <= len(ice_box) - 1 and 0 <= ny <= len(ice_box[0]) - 1 and visited[nx][ny] is False and ice_box[nx][ny] == ICE:
            dfs(ice_box, (nx, ny), visited)


print(solution(test_case_1))


def solution_in_book(ice_box):
    n = len(ice_box)
    m = len(ice_box[0])

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs_in_book(ice_box, i, j) == True:
                result += 1

    return result


def dfs_in_book(ice_box, i, j):
    n = len(ice_box)
    m = len(ice_box[0])
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if ice_box[i][j] == 1:
        return False

    ice_box[i][j] = 1

    for t in range(MOVE_TYPES_COUNT):
        ni = i + DIR_X[t]
        nj = j + DIR_Y[t]
        dfs_in_book(ice_box, ni, nj)

    return True


print(solution_in_book(test_case_1.copy()))