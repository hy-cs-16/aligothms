DIR = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0),
}


class User:
    def __init__(self, map_size):
        self.x = 1
        self.y = 1
        self.map_size = map_size

    def move(self, direction):
        dx, dy = DIR[direction]

        next_x = self.x + dx
        next_y = self.y + dy

        if 1 <= next_x <= self.map_size and 1 <= next_y + dy <= self.map_size:
            self.x = next_x
            self.y = next_y

    def pos(self):
        return self.x, self.y


def solution(n, plans):
    user = User(n)

    for plan in plans:
        user.move(plan)

    return user.pos()


result1 = solution(5, 'R R R U D D'.split(' '))
assert result1 == (3, 4)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


def solution_in_book(n, plans):
    x, y = 1, 1

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        x, y = nx, ny

    return x, y