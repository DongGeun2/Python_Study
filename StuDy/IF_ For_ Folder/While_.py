# while  = 조건이 만족할때까지 반복
customer = "토르"
index = 5
while index >= 1:    # 조건이 만족될때까지 반복 index = 5 이니깐 index가 0이 될때까지 반복
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")


# customer = "아이언맨"
# while True:
#      print("{0}, 커피가 준비 되었습니다..".format(customer))
# 무한루프 벗어나오는 법  ctrl + c


# customer = "토르"
# person = "동구"

# while person != customer : 
#     print("{0}, 커피가 준비 되었스빈다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
