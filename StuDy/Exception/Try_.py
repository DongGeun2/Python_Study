
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print("에러! 0으로는 나눌수 없습니다.")




# try 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행



