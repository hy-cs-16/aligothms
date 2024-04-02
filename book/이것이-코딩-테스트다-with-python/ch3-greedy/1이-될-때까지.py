def solution(n, k):
    count = 0
    while n != 1:
        count += 1

        if n % k == 0:
            n //= k
        else:
            n -= 1

    return count

def solution_in_book(n, k):
    result = 0

    while n >= k:
        while n & k != 0:
            n -= 1
            result += 1

        n //= k
        result += 1

    while n > 1:
        n -= 1
        result += 1

    return result