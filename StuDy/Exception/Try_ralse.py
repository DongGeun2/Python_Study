class Bignumbererror(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg



try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise Bignumbererror("입력값 : {0}, {1}".format(num1,num2)) # 강제 오류 만들기 raise
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러 ~")
except Bignumbererror as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다")





 