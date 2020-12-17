# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 확실히 모름.
# len(some_list)가 0이나 1이 나와야 base case
# 0이나 1인 리스트를 뒤집으면 리스트 자체
# some_list[-1:]와 flip(some_list[:-1])