# Tabulation
def max_profit(price_list, count):
    profit_table = [0]

    for i in range(1, count + 1):
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])
        profit_table.append(profit)
    return profit_table[count]

# Memoization
def max_profit_memo(price_list, count, cache):
    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                     + max_profit_memo(price_list, count - i, cache))
    cache[count] = profit

    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))