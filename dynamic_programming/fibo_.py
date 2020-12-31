# Memoization
def fib_memo(n, cache):
    # 코드를 작성하세요.
    if n < 3:
        return 1
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# Tabulation
def fib_tab(n):
    fib_table = [0, 1, 1]

    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    return fib_table[n]

## 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))


# fibo_ 공간 최적화 O(1)
def fib_optimized(n):
    current = 1
    previous = 0
    for i in range(1, n):
        current, previous = current + previous, current

    return current

print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
