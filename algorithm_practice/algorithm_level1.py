# Brute Force
# 최대 수익 계산

def sublist_max(profits):
    max_profit = profits[0]

    for i in range(len(profits)):
        total = 0
        for j in range(i, len(profits)):
            total += profits[j]
            max_profit = max(max_profit, total)

    return max_profit

print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))

# recursion
# O(lg y) 거듭 제곱 계산

def power(x, y):
    if y == 0:
        return 1
    # 계산을 한 번만 하기 위해서 변수에 저장
    tmp = power(x, y // 2)
    # 문제를 최대한 똑같은 크기의 문제 두 개로 나눠준다 (짝수, 홀수 경우 따로)
    if y % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp

print(power(3, 5))
print(power(5, 6))
print(power(7, 9))

# greedy_algorithm

def select_stops(water_stops, capacity):
    stop_list = []
    prev = 0
    for i in range(len(water_stops)):
        if water_stops[i] - prev > capacity:
            stop_list.append(water_stops[i - 1])
            prev = water_stops[i - 1]
    stop_list.append(water_stops[-1])

    return stop_list

list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))
list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))

# dictionary, list

def find_same_number(some_list):
    prev_elements = {}
    for element in some_list:
        if element in prev_elements:
            return element

        prev_elements[element] = True

    # tmp = {}
    # for i in range(len(some_list)):
    #     if some_list[i] not in tmp:
    #         tmp[some_list[i]] = i
    #     else:
    #         return some_list[i]

print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))