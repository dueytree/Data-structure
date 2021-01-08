# find_same_number
def find_same_number(some_list, start=1, end=None):
    if end == None:
        end = len(some_list) - 1

    if start == end:
        return start

    middle = (start + end) // 2
    left = 0
    for element in some_list:
        if start <= element and element <= middle:
            left += 1

    if left > middle - start + 1:
        return find_same_number(some_list, start, middle)
    return find_same_number(some_list, middle + 1, end)


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

## um_in_list

def sum_in_list(search_sum, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low < high:
        candidate_sum = sorted_list[low] + sorted_list[high]

        if candidate_sum == search_sum:  # 합이 찾으려는 숫자일 때
            return True

        if candidate_sum < search_sum:  # 합이 찾으려는 숫자보다 작을 때
            low += 1

        else:  # 합이 찾으려는 숫자보다 클 때
            high -= 1

    # 찾는 조합이 없기 때문에 False 리턴
    return False


# 테스트
print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))