def consecutive_sum(start, end):
    # base case
    if end == start:
        return start
    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정리한다(Divide).
    middle = (start + end) // 2
    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더한다(Combine).
    return consecutive_sum(start, middle) + consecutive_sum(middle + 1, end)

print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))