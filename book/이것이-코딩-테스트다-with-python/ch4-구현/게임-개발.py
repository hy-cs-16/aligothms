# N, E, S, W
# x: 행 \ y: 열
DIR_X = [-1, 0, 1, 0]
DIR_Y = [0, 1, 0, -1]
move_types = [0, 1, 2, 3]
# N을 바라보면, W
# W를 바라보면, S
# S를 바라보면, E
# E를 바라보면, N
GROUND = 0
WATER = 1


def is_in_playground(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

class Player:
    def __init__(self, playground, pos_x, pos_y, dir):
        self.x = pos_x
        self.y = pos_y
        self.dir = dir
        self.playground = playground
        self.n = len(playground)
        self.m = len(playground[0])
        self.visited = [len(row) * [False] for row in playground]
        self.visited[self.x][self.y] = True
        self.dir_change = 0
        self.stopped = False

    def movable(self):
        dx = DIR_X[self.dir]
        dy = DIR_Y[self.dir]

        nx = self.x + dx
        ny = self.y + dy

        return is_in_playground(nx, ny, self.n, self.m) and self.visited[nx][ny] is False and self.playground[nx][ny] == GROUND

    def turn_left(self):
        self.dir = (self.dir - 1) % 4
        self.dir_change += 1
        # print(f"현위치 ({self.x},{self.y}) 왼쪽으로 돌기 [지금 보고있는 방향: {list('북동남서')[self.dir]}]")

    def go_forward(self):
        # print(f"현위치 ({self.x},{self.y}) {list('북동남서')[self.dir]} 방향으로 한칸 전진 ")
        dx = DIR_X[self.dir]
        dy = DIR_Y[self.dir]

        nx = self.x + dx
        ny = self.y + dy

        self.dir_change = 0
        self.x = nx
        self.y = ny
        self.visited[nx][ny] = True

    def go_back(self):
        dx = DIR_X[(self.dir - 2) % 4]
        dy = DIR_Y[(self.dir - 2) % 4]

        nx = self.x + dx
        ny = self.y + dy

        if is_in_playground(nx, ny, self.n, self.m) and self.playground[nx][ny] == GROUND:
            # print(f"{list('북동남서')[(self.dir - 2) % 4]} 방향으로 한칸 후진")
            self.dir_change = 0
            self.x = nx
            self.y = ny
        else:
            # print('후진 불가능 종료')
            self.stopped = True


def solution(playground, pos_x, pos_y, dir):
    player = Player(playground, pos_x, pos_y, dir)

    while player.stopped is False:
        player.turn_left()

        if player.movable():
            player.go_forward()
        elif player.dir_change == 4:
            player.go_back()

    count = 0
    for row in player.visited:
        for visit in row:
            if visit is True:
                count += 1

    return count

result1 = solution([
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
],1, 1, 0)
print(result1)
assert result1 == 3

result2 = solution([
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 0]
],0, 2, 0)
print(result2)
assert result2 == 1

def solution_in_book():
    pass
