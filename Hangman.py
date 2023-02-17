import os
import random

os.chdir(r'C:\Users\한률\Desktop\Drone_Coding\Practice')

word_list = []

def find_word():
    with open("word.txt", "r") as f:
        lines = f.readlines()
        # ['apple:사과\n', 'banana:바나나\n', 'cat:고양이\n', 'desk:책상\n']   

    for line in lines:
        word = line.split("\n")[0].split(":")[0]
        word_list.append(word)
        
    return(word_list)

def quiz(quiz_word):
    answer = quiz_word
    your_choice = list("_" * len(answer)) # ['_', '_', '_', '_', '_']
    count = 6
    is_answer = False
    
    while count > 0:
        print(f"{count}번째 기회가 남았습니다.")
        show_choice = " ".join(your_choice)
        print(show_choice) # _ _ _ _ _
        
        your_input = input("알파벳을 입력하세요 : ")
        find_count = 0

        for i in range(len(answer)):
            if your_input == answer[i]:
                your_choice[i] == your_input
                find_count += 1
            
        if find_count == 0:
            count -= 1
            
        show_choice = "".join(your_choice)
        print(show_choice)

        if show_choice == answer:
            print("☆★정답을 맞혔습니다☆★")
            global my_score
            global score
            my_score += score
            break
            
        if count == 0:
            print("정답을 못 맞혔습니다.")
            break
        print("======")

quiz_count = 5
total_count = quiz_count
my_score = 0
score = 10
words = find_word()

print(f"행맨 문제가 {quiz_count} 나옵니다.")
while quiz_count > 0:
    print(f"{total_count - quiz_count + 1}번째 문제입니다.")
    choice_word = random.choice(words)
    quiz(choice_word)
    quiz_count -= 1

print(f"점수는 {my_score}점 입니다.")