# 2024 Apr 1 5:30 PM START
# 누적 값을 acc[] 로 들고있고 O(n)
# acc 는 정렬이 되어 있으므로
# 첫번째 acc 값을 기반으로, k 를 만들 수 있는 오른쪽 인덱스값을 찾는다. O(logN) -> binary search
#   없으면, 왼쪽 인덱스 값 += 1
#   찾으면, 리턴
# 2024 Apr 1 5:35 PM 알고리즘 구현 시작
# 2024 Apr 1 5:55 PM 알고리즘 구현 완료 -> 문제 잘못 봄...


def solution(sequence, k):
    # memorization acc
    acc = [sequence[0]]
    for i in range(1, len(sequence)):
        acc.append(acc[i - 1] + sequence[i])
    # index : left
    # value : 부분합이 k 를 만족하는 최소의 right,
    # right 가 -1 이면 left 가 index 인 부분합은 존재하지 않는다
    indexes = []

    right_index = binary_search(acc, k, 0, len(sequence) - 1)
    if right_index != -1:
        print(right_index)
        indexes.append([0, right_index])

    for left in range(1, len(sequence)):
        print('left', left)
        target_value = k - acc[left - 1]
        right_index = binary_search(acc, target_value, left, len(sequence) - 1)
        found = right_index != -1
        if found:
            indexes.append([left, right_index])
    print(acc)
    print(indexes)
    answer = [0, len(sequence)]
    for index in indexes:
        curr = answer[1] - answer[0]
        temp = index[1] - index[0]
        if curr > temp:
            answer = index
        elif curr == temp:
            if index[0] < answer[0]:
                answer = index

    return answer


def binary_search(arr, value, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if value == arr[mid]:
        return mid
    elif value > arr[mid]:
        return binary_search(arr, value, mid + 1, right)
    else:
        return binary_search(arr, value, left, mid - 1)


# 2024 Apr 1 5:30 PM START
# 누적 값을 acc[] 로 들고있고 O(n)
# acc 는 정렬이 되어 있으므로
# 첫번째 acc 값을 기반으로, k 를 만들 수 있는 오른쪽 인덱스값을 찾는다. O(logN) -> binary search
#   없으면, 왼쪽 인덱스 값 += 1
#   찾으면, 리턴
# 2024 Apr 1 5:35 PM 알고리즘 구현 시작
# 2024 Apr 1 5:55 PM 알고리즘 구현 완료 -> 문제 잘못 봄...

from collections import deque


def solution(sequence, k):
    # memorization acc
    acc = deque([0, sequence[0]])
    for i in range(1, len(sequence)):
        acc.append(acc[i - 1] + sequence[i])

    left = 0
    right = 0

    while True:
        left_value = acc.popleft()
        print('lv:', left_value)
        print('find: ', k - left_value)
        arr = list(acc)

        right = binary_search(arr, k - left_value, 0, len(arr))
        print(arr, left, left + right)
        if right == -1:
            left += 1
        else:
            break

    return [left, left + right]


def binary_search(arr, value, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if value == arr[mid]:
        return mid
    elif value > arr[mid]:
        return binary_search(arr, value, mid + 1, right)
    else:
        return binary_search(arr, value, left, mid - 1)
