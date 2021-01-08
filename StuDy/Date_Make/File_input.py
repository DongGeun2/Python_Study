score_file = open("score_file", "w", encoding="utf8")   # w(wriet)= 쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score_file", "a", encoding="utf8")   # a(add) = 덮어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()


score_file = open("score_file", "r", encoding="utf8")   # r(read) = 읽기 
print(score_file.read())

score_file = open("score_file", "r", encoding="utf8")
print(score_file.readline())                            # readline 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score_file", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

score_file = open("score_file", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line)




# w(wriet)= 쓰기  a(add) = 덮어쓰기 r(read) = 읽기 