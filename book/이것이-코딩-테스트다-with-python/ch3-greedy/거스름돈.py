def solution(N: int):
    coins = [500, 100, 50, 10]

    count = 0
    while count <= N:
        coin = coins.pop()

        count += N // coin
        N %= coin

    return count


def solution_in_book(N: int):
    coins = [500, 100, 50, 10]

    count = 0
    for coin in coins:
        count += N // coin
        N %= coin

    return count

