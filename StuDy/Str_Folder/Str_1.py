strs = "나는 학생입니다."
print(strs)
strs1 = "나는 5학년입니다."
print(strs1)


strs2 = """
나는 학생이고
나는 5학년입니다.
"""
print(strs2)


#---------------------------------------
# slicing
jumin = "951015-1234567"

print("성별 : " + jumin[7]) # 7번째 = 1
print("연 : " + jumin[0:2]) # 0~2 = 95
print("월 : " + jumin[2:4]) # 2~4 = 10
print("일 : " + jumin[4:6]) # 4~6 = 15

print("생년월일 : " + jumin[:6]) # 0~6 = 951015
print("뒷번호 : " + jumin[7:]) # 7 ~ 끝까지 = 1234567 
print("뒷번호 (뒤에서부터) : " + jumin[-7:]) # 뒤에서 붙어 7번째 까지 = 1234567