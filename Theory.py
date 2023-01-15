## 9주차

# lambda
a = lambda x, y : x + y
print(a(5,5))

# filter(내장함수) : 조건에 맞는 원소 구하기
a = [1, 2, 3, 4]
print(list(filter(lambda x : x > 3, a)))

# map : 원소를 하나씩 처리
a = [1, 2, 3, 4]
b = list(map(lambda x : x * 2, a))
print(b) 

# *args : 여러 개의 인자를 받아서 처리(튜플)
def manyArguments(*args):
    sum_value = 0
    for item in args:
        sum_value += item
    return sum_value

a = manyArguments(12, 28, 21, 23)
print(a)

# 지역변수(local variable) : 함수 내에서 쓰이는 변수
# 전역변수(global variable) : 함수 밖에서 쓰이는 변수

a = 10 # (global)
def test():
    a = 20
    print(a)
test() # 20(local)
print(a) # 10(global)

a = 10
def test():
    global a # local -> global
    a = 20
    print(a)
test()
print(a)