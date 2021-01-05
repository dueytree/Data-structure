## O(nlgn)
def max_crossing_sum(profits, start, end):
    # 코드를 작성하세요.
    mid = (start + end) // 2
    '''
    왼쪽에서의 가장 큰 수익 계산
    인덱스 mid부터 인덱스 0까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    left_sum = 0
    left_max = profits[mid]

    for i in range(mid, start - 1, -1):
        left_sum += profits[i]
        left_max = max(left_max, left_sum)
    '''
    오른쪽에서의 가장 큰 수익 계산
    인덱스 mid+1부터 인덱스 end까지 범위를 넓혀가며 최대 수익을 찾는다
    '''
    right_sum = 0
    right_max = profits[mid + 1]

    for i in range(mid + 1, end + 1):
        right_sum += profits[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def sublist_max(profits, start, end):
    if start == end:
        return profits[start]
    mid = (start + end) // 2
    max_left = sublist_max(profits, start, mid)
    max_right = sublist_max(profits, mid + 1, end)
    max_cross = max_crossing_sum(profits, start, end)

    # 위 세 경우 중 가장 큰 결괏값을 리턴한다
    return max(max_left, max_right, max_cross)


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))

## O(n)
def sublist_max(profits):
    # 코드를 작성하세요.
    max_profit_so_far = profits[0]  # 반복문에서 현재까지의 부분 문제의 답
    max_check = profits[0]  # 가장 끝 요소를 포함하는 구간의 최대 합

    # 반복문을 통하여 각 요소까지의 최대 수익을 저장한다
    for i in range(1, len(profits)):
        # 새로운 요소를 포함하는 구간의 최대합을 비교를 통해 정한다
        max_check = max(max_check + profits[i], profits[i])

        # 최대 구간 합을 비교를 통해 정한다
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far


# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))

## max_profit
def max_profit(stock_list):
    # 코드를 작성하세요.
    profit = stock_list[1] - stock_list[0]

    min_stock = min(stock_list[0], stock_list[1])

    for i in range(2, len(stock_list)):
        profit = max(profit, stock_list[i] - min_stock)

        min_stock = min(min_stock, stock_list[i])

    return profit

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))

## staircase1
def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

## staircase2
def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    number = [1, 1]

    for h in range(2, stairs + 1):
        number.append(0)

        for step in possible_steps:
            if h - step >= 0:
                number[h] += number[h - step]

    return number[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))