## dictionary
grades = {}

# key - value 데이터 삽입
grades["현승"] = 80
grades["태호"] = 60
grades["영훈"] = 90
grades["지웅"] = 70
grades["동욱"] = 96

print(grades)  # 딕셔너리 출력

# 한 key 에 여러 value 저장 시도
grades["태호"] = 100

print(grades)  # 딕셔너리 출력

# key 를 이용해서 value 탐색
print(grades["동욱"])
print(grades["지웅"])

# key 를 이용한 삭제
grades.pop("태호")
grades.pop("지웅")

print(grades)  # 딕셔너리 출력

## set
finished_classes = set()

finished_classes.add("자료 구조")
finished_classes.add("알고리즘")
finished_classes.add("프로그래밍 기초")
finished_classes.add("인터렉티브 웹")
finished_classes.add("데이터 사이언스")

print(finished_classes)  # 세트 출력

# 중복 데이터 저장 시도
# finished_classes.add("자료 구조")
# finished_classes.add("알고리즘")
#
# print(finished_classes)  # 세트 출력

# 데이터 탐색
print("컴퓨터 개론" in finished_classes)
print("자료 구조" in finished_classes)

# 데이터 삭제
finished_classes.remove("자료 구조")
finished_classes.remove("알고리즘")

print(finished_classes)  # 세트 출력