# import travel.korea      # improt 모듈이나 클래스만 사용가능 ( 함수 불가능 )
# trip = travel.korea.koreapackage()
# trip.koreas()

# from travel import korea
# hello = korea.koreapackage()
# hello.koreas()

from travel import * 
# # hello = korea.koreapackage()
# # hello.koreas()



import inspect
import random
print(inspect.getfile(random))

