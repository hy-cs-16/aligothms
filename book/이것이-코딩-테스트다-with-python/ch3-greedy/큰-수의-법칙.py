def solution(M: int, K: int, nums: list[int]):
    descending_nums = sorted(nums, key=lambda x: x, reverse=True)

    first_max = descending_nums[0]
    second_max = descending_nums[1]

    largest_num = 0

    count = 0
    count_k = 0
    while count < M:
        if count_k < K:
            largest_num += first_max
        else:
            largest_num += second_max
            count_k = 0
        count += 1

    return largest_num


def solution_in_book(M: int, K: int, nums: list[int]):
    nums.sort()
    first = nums[len(nums) - 1]
    second = nums[len(nums) - 2]

    result = 0

    while True:
        for i in range(K):
            if M == 0:
                break
            result += first
            M -= 1

        if M == 0:
            break
        result += second
        M -= 1

    return result

