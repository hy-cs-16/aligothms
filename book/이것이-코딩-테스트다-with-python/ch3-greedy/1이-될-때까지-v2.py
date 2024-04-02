def solution(n, k):
    count = 0
    while n >= 1:
        if n % k == 0:
            n //= k
            count += 1
        else:
            # n 이 0 이 될 때까지 동작 한다
            mod = n % k
            n -= mod
            count += mod

    # 1 이 될 때까지 이므로, 1 을 빼주면 된다.
    return count - 1


def solution_in_book(n, k):
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target

        if n < k:
            break

        result += 1
        n //= k

    # 마지막 으로 남은 수에 대해서 1씩 빼기
    while n > 1:
        n -= 1
        result += 1

    return result