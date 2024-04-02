import time


def solution(n):
    count_seconds_not_include_3 = [str(x) for x in range (0, 60) if str(x).find('3') == -1]
    count_minutes_not_include_3 = [str(x) for x in range(0, 60) if str(x).find('3') == -1]
    count_hours_not_include_3 = [str(x) for x in range(0, n + 1) if str(x).find('3') == -1]

    return 60 * 60 * (n + 1) - len(count_hours_not_include_3) * len(count_minutes_not_include_3) * len(count_seconds_not_include_3)

result1 = solution(5)
assert result1 == 11475


def solution_in_book(n):

    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    return count
result1 = solution_in_book(5)
assert result1 == 11475

