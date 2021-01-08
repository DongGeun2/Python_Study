cabinet = {1:"김치찌개", 100:"된장찌개"}   # 키 활용
print(cabinet[1])
print(cabinet[100])

print(cabinet.get(1))
print(cabinet.get(5))  # 값이 없으면 None 값 출력


print(1 in cabinet) # true
print(5 in cabinet) # false

# key 만 출력
print(cabinet.keys())

# value 만 출력
print(cabinet.values())

# key , value 둘다 출력
print(cabinet.items())

# 모두 제거
cabinet.clear
print(cabinet)