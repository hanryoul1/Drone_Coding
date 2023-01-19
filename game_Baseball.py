# 숫자 야구 프로그램 만들기

import random

size = 3 # 자릿수
number_choice = random.sample(range(1,10), size)
count = 0
strike_count = 0
ball_count = 0

print("=== 숫자야구를 시작합니다 ===")
print("1부터 9까지의 숫자를 사용해서 %d자리수를 만들었습니다." % size)
print("숫자는 맞혔지만, 자리수가 다르면 볼(ball)입니다.")
print("숫자랑 자리수를 모두 맞히면 스트라이트(strike)입니다.")

def check_number():
    global strike_count
    global ball_count
    global count
    strike_count = 0
    ball_count = 0
    count += 1
    for i in range(size):
        for j in range(size):
            if (number_choice[i] == int(number[j]) and i == j):
                strike_count += 1
            
            elif (number_choice[i] == int(number[j]) and i != j):
                ball_count += 1
        
    print("스트라이크: ", strike_count, "/", "볼: ", ball_count)
    print("%d번 입력했습니다." % count)
    print("==========")

while (strike_count < size):
    number = input("숫자를 입력하세요 : ")
    if(number.isdecimal()): # isdecimal() : 숫자인지 아닌지 확인
        number = str(number)
        if (len(number) == size):
            is_same = False
            for i in range(len(number)-1):
                for j in range(i+1, len(number)):
                    if number[i] == number[j]:
                        is_same = True
                        break
            if not is_same:
                check_number()
            else:
                print("숫자를 다시 입력하세요.")
                continue
        else:
            print("숫자를 다시 입력하세요.")
    else:
        print("숫자를 다시 입력하세요.")