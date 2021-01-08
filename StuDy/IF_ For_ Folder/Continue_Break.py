absent = [2, 5] # 결석
no_book = [7] # 책 안갖고옴

for student in range(1,11):
    if student in absent:
        continue         # 더이상 그 문장을 실행하지 않고 다음 반복문 실행
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와".format(student))
        break            # 더이상 그 문장을 실핼하지 않고 반복문 종료
    print("{}, 책을 읽어봐".format(student))
