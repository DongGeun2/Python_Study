# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)


print(subway.index(30)) # 30이 몇번째에 있는지 

subway.append(60)     # 제일 뒤에 추가
print(subway)

subway.insert(1, 70)  # 몇번째 , 무엇을 추가할지
print(subway)

print(subway.pop())   # 한개씩 뒤에서 뺌
print(subway)

subway.append(10)
print(subway)
print(subway.count(10))  # 같은값 몇번 나오는지 확인

# 정렬
num_list = [5,3,4,1,2]
num_list.sort()   # sort = 정렬
print(num_list)

# 순서뒤집기
num_list.reverse() # reverse = 뒤집기
print(num_list)

# 모두지우기
num_list.clear()
print(num_list)


