def solution(arr: list[list[int]]):

    min_in_rows = list(map(lambda row: min(*row), arr))

    return max(*min_in_rows)

def solution_in_book(arr: list[list[int]]):
    result = 0
    for i in range(len(arr)):
        min_value = min(arr[i])

        result = max(result, min_value)

    return result
