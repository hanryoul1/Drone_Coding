""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# <9주차>
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
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# <10주차>
# 클래스
class MyClass():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self): # self = instance 자신
        print(f"내 이름은 {self.name}입니다.")
        print(f"내 나이는 {self.age}살입니다.")

a = MyClass("파이썬", 10) # 객체(instance)
b = MyClass("드론", 20) 

a.print_info()
b.print_info()

print(id(a)) # 메모리 주소
print(id(b))

# 클래스 상속
class Parent():
    def __init__(self, name):
        self.name = name
    
class Child(Parent):
    pass

a = Child("알파코")
print(a.name)

# Overriding
class Animal():
    def say(self, message):
        print(message)

class Dog(Animal):
    def say(self, message):
        print("멍멍") # Overriding(method)
    
a = Animal()
b = Dog()

a.say("안녕")
b.say("안녕")

# Drone Class
class Drone():
    def __init__(self, color, weight, speed):
        self.color = color
        self.weight = weight
        self.speed = speed

    def show_info(self):
        print(f"색깔은 {self.color}입니다.")
        print(f"무게는 {self.weight}kg입니다.")
        print(f"속도는 {self.speed}입니다.")

    def set_info(self, color, weight, speed):
        self.color = color
        self.weight = weight
        self.speed = speed

    def take_off(self):
        print("이륙합니다.")

class Codrone(Drone):
    def pitch(self):
        print("빠르게 앞으로 이동합니다.")

a = Drone("노란", 3, 3)
b = Codrone("파란", 5, 5)

a.set_info("빨강", 4, 4)
a.show_info()
a.take_off()

b.show_info()
b.pitch()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# <11주차>
# 모듈과 패키지
# 파일 하나 = 모듈
# 모듈을 폴더 구조로 관리 = 패키지
# 패키지를 사용할 수 있도록 하는 것 = 라이브러리

# 1) 폴더 - 폴더 - 파일
import module.name.name
import module.age.age

# 2) from module.name.name import 변수, 함수
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# <12주차>
# file
# r : 읽기모드(read) 파일을 읽기만 할 때 사용
# w : 쓰기모드(write) 파일에 내용을 쓸 때 사용(전부 지우고 새롭게)
# a : 추가모드(append) 파일의 마지막에 새로운 내용을 추가할 때 사용

import os
os.chdir(r"C:\Users\한률\Desktop\Drone_Coding") 
# chage directory
# C:// -> C:/
print(os.getcwd()) # 경로 확인
# f = open("file.txt", "w")
f = open("file.txt", "a")
f.write("\nPython Coding")
f.close()

# try & except
# try : 해야할 것
# excepy : 오류가 생겼을 때 해야할 것

# r 모드
# readline : 한 줄씩 읽기 / 읽다가 줄이 없으면 종료
# readlines : 여러 줄 읽기