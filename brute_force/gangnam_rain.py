def trapping_rain(buildings):
    # 코드를 작성하세요
    tmp = 0

    for i in range(1, len(buildings) - 1):
        left = max(buildings[:i])
        right = max(buildings[i:])

        sum_rain = min(left, right)

        tmp += max(0, sum_rain - buildings[i])
    return tmp

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))