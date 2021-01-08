# 변경되지 않을 항목 사용할 경우 튜플 사용

meun = ("돈까스", "치즈까스")
print(meun[0])
print(meun[1])

# 튜플은 add 불가

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

