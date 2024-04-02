# 좌상, 좌하, 하좌, 하우, 우상, 우좌, 상좌, 상우
DIRS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]

def solution(start):
    now = tuple(start)
    col = int(ord(now[0])) - int(ord('a')) + 1
    row = int(now[1])

    count = 0
    for dir in DIRS:
        dc, dr = dir
        next_col = col + dc
        next_row = row + dr

        if 1 <= next_col <= 8 and 1 <= next_row <= 8:
            count += 1

    return count


result1 = solution('a1')
assert result1 == 2

def solution_in_book():
    pass
