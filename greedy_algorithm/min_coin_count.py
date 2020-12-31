# 최소 동전 거슬러주기
def min_coin_count(value, coin_list):
    count = 0
    for coin in sorted(coin_list, reverse=True):
        count += (value // coin)

        value %= coin
    return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))


# 최대 곱 구하기
def max_product(card_lists):
    product = 1
    for card_list in card_lists:
        product *= max(card_list)

    return product

# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))


# 지각 벌금 적게 내기
def min_fee(pages_to_print):
    sorted_list = sorted(pages_to_print)
    total_fee = 0

    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)
    return total_fee

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
