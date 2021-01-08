print("python","java\t", sep=",",end="?")
print("무엇이 더 재밌을까요?")

import sys
print("python", "java", file=sys.stdout)            # 표준출력 
print("python", "java", file=sys.stderr)            # 표준에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(5), str(score).rjust(5), sep =":")   # ljust = 왼쪽정렬 , rjust = 오른쪽정렬

# 은행 대기 순번표
# 001,002,003, ...
for num in range(1,4):
    print("대기번호 : " + str(num).zfill(3))


answer = input("아무 값이나 입력하세요 : ")   # input 은 항상 문자열(str)으로 출력
print("입력하신 값은 " + answer + "입니다.")
