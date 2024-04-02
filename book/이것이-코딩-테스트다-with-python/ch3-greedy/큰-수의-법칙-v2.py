def solution(m: int, k: int, nums: list[int]):
    descending_nums = sorted(nums, key=lambda x: x, reverse=True)

    first_max = descending_nums[0]
    second_max = descending_nums[1]

    cycle_size = k + 1
    cycle_sum = first_max * k + second_max
    cycle_count = m // cycle_size
    remain_size = m % cycle_size

    return cycle_sum * cycle_count + remain_size + first_max


def solution_in_book(m: int, k: int, nums: list[int]):
    nums.sort()
    first = nums[len(nums) - 1]
    second = nums[len(nums) - 2]

    count = int(m / (k + 1)) * k
    count += m % (k + 1)

    return count * first + (m - count) * second
