def max_product(left_cards, right_cards):
    tmp = []
    for left in left_cards:
        for right in right_cards:
            tmp.append(left * right)

    return max(tmp)


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))