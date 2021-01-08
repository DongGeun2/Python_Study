# 집합 (set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)   # {1,2,3}

java = {"유재석","김태호","양세형"}
python = set(["유재석","김종국"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 (자바는 할수 있지만 파이썬은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# 파이썬 할줄 아는 사람 늘어남
python.add("김태영")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)
