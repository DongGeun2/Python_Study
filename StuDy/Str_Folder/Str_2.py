# print("a" + "b")


# 방법 1 
print("나는 %d살입니다." % 20)   # %d 는 정수값
print("나는 %s을 좋아해요." % "파이썬") # %s 는 문자열 (str)  
print("apple 은 %c 로 시작해요." % "a") # %c 는 한글자

print("나는 %s살 이고, %s입니다." %(20,"남자")) # 괄호안에 순서대로 입력


# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {0}살 이고, {1}입니다.".format(20,"남자")) # {0},{1} 순서 인식

# 방법 3
print("나는 {age}살 이며, {color}색을 좋아해요".format(age = 20, color ="빨간"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살 이며, {color}색을 좋아해요") 

