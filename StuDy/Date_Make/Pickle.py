# pickle ()     

import pickle

profile = open("donggo.pickle", "wb")        # pickle을 쓰기위해선 b(바이너리)를 무조건 입력해야한다.
donggo = {"이름 : 동구", "나이 : 26살"}
# print(donggo)

pickle.dump(donggo,profile)  # donggo 의 정보를 프로필에 저장
profile.close()



