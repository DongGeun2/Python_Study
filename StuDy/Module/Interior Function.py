
# 내장 함수

# input : 사용자 입력을 받는 함수

# dir : 어떤 객체가 넘겨줬을 때 그 객체가 어떤 변수 와 함수를 가지고 있는지 표시



# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# # os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리


# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

import time # 시간 관련 함수
print(time.localtime())
print(time.strftime("%Y-%m-%d"))

import datetime
print("오늘 날짜는 " , datetime.date.today())

# 날짜 사이 간격
todat = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100)
print(todat + td)