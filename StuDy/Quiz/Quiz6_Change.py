
class nothuman(Exception):
    pass


def std_weight2(height,gender):
    try:
        if gender == "남자":
            weight = round((height / 100) * (height / 100) * 22,2)
            print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,weight))
            return height, gender
        elif gender == "여자":
            weight = round((height / 100) * (height / 100) * 21,2)
            print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,weight))
            return height, gender
        else:
            raise nothuman
    except nothuman:
        print("남자 or 여자의 값만 넣어주세요.")


std_weight2(175,"남자")
std_weight2(160,"여자")
std_weight2(159,"사람")



