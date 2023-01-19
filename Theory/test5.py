import os
os.chdir(r"C:\Users\한률\Desktop\Drone_Coding")

# with open("test_file.txt", "r") as r:
#     while True:
#         line = r.readline() # readline : 한 줄 씩 읽기
#         if not line:
#             break
#         print(line)

with open("test_file.txt", "r") as r:
    lines = r.readlines() # readlines : list로 읽기
    print(lines)