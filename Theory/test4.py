import os

os.chdir(r'C:\Users\한률\Desktop\Drone_Coding\Practice')

while True:
    try:
        word = input("영어단어 : ")
        meaning = input("그 뜻은 무엇인가요? : ")
        with open("word.txt", "a") as f:
            f.write(word)
            f.write(":")
            f.write(meaning)
            f.write("\n")
    except:
        pass
              
    your_input = input("입력을 그만하고 싶으면 'q'키를, 그렇지 아니면 다른 키를 누르세요: ")
    if your_input == "q":
        break
    else:
        continue
    
print("단어를 다 입력했습니다.")