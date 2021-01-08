import pickle

profile = open("donggo.pickle", "rb")
donggo = pickle.load(profile) # 프로필에 있는 정보를 동구에 불러오기
profile.close()
