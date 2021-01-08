python = "Python is very Good"

print(python.lower()) # 소문자출력 = python is very good

print(python.upper()) # 대문자출력 = PYTHON IS VERY GOOD

print(python[0].isupper()) # 0번째 값이 대문자가 맞는지 확인 = True

print(len(python)) # 문자길이반환 출력 = 19

print(python.replace("Python", "Java"))  # 문자 바꾸기 = Java is very Good

print(python.index("o")) # o 라는 글자가 몇번째 있는지 출력 = 7

print(python.find("o")) # o 라는 글자가 몇번째 있는지 출력 = 7
# ※find 함수는 만약 글자가 포함하지않을시 -1을 출력하게 된다

print(python.count("o")) # o 라는 글자가 몇개 있는지 출력 = 3

