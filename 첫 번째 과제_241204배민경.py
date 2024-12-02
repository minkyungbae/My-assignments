### 과제1
# 1. 플레이어와 컴퓨터가 참여하는 숫자 맞추기 게임을 만드세요. 
# 2. 프로그램은 다음과 같은 기능을 포함해야 합니다.
# - 컴퓨터는 1부터 10 사이의 랜덤한 숫자를 생성합니다.
# - 플레이어는 숫자를 입력하고, 입력한 숫자가 큰지 작은지 힌트를 얻습니다.
# - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다.

# 조건
# 1과 10 사이의 숫자를 하나 정했습니다.
# 이 숫자는 무엇일까요?
# 예상 숫자: 5
# 너무 큽니다. 다시 입력하세요.
# 예상 숫자: 4
# 너무 큽니다. 다시 입력하세요.
# 예상 숫자: 3
# 정답입니다!


import random

input_random_numbers = random.randint(1, 10)
print(input_random_numbers)

# while True:
     start_sentence = int(input("숫자를 입력해주세요: "))
     if input_random_numbers == start_sentence:
         print("정답입니다!")
         break
     elif start_sentence < input_random_numbers:
         print("보다 큽니다, 다시 입력해주세요!")
     elif start_sentence > input_random_numbers:
         print("보다 작습니다, 다시 입력해주세요!")
     else:
         print("땡! 다시 입력해주세요")


        
# 함수 ver.
# import random

# def random_game_start():
#     input_random_numbers = random.randint(1, 10)
#     print(input_random_numbers)

#     while True:
#         start_sentence = int(input("숫자를 입력해주세요: "))
#         if input_random_numbers == start_sentence:
#             print("정답입니다!")
#             break
#         elif start_sentence < input_random_numbers:
#             print("보다 큽니다, 다시 입력해주세요!")
#         elif start_sentence > input_random_numbers:
#             print("보다 작습니다, 다시 입력해주세요!")
#         else:
#             print("땡! 다시 입력해주세요")
            
# random_game_start()



### 과제2
# 1트
#class 자체가 함수(?)였네!!!!
# 클래스(=객체) 정의 - member 변수랑 함수로 이루어짐
# class person:
#     def members_information():
#         name = "personal_informations_name"
#         gender = "personal_informations_gender"
#         age = "personal_informations_age"


# 2트 -> 두 번째 def가 정의 잘 된 거 아닌가? 왜 프린트 안 됨?
# class person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
        
#     def person_informaitons():
#         person_informations = person()
#         person_informations.name = input("이름을 입력해 주세요 -> ")
#         person_informations.gender = input("성별을 입력해 주세요 -> ")
#         person_informations.age = int(input("나이를 입력해 주세요 -> "))



# 3트
# class person:
#     def __init__(self, name, gender, age):
#         self.name = input("이름을 입력해 주세요 -> ")
#         self.gender = input("성별을 입력해 주세요 -> ")
#         self.age = int(input("나이를 입력해 주세요 -> "))
        
#     def person_information():
#         person_information = person()



# 4트
class person:
    def __init__(self):
        self.name = input("이름을 입력해주세요 -> ")
        self.gender = input("성별을 입력해주세요 -> ")
        self.age = int(input("나이를 입력해주세요 -> "))
    def display(self):
        # format을 쓸 때 {}를 넣어야 변수값이 들어감
        print("이름 : {}, 성별 : {}, 나이 : {}".format(self.name, self.gender, self.age))
        # print("이름 : ", self.name, "성별 : ", self.gender, "나이 : ", self.age)
        # show() = dispaly()
        
# 객체 생성(=person_info)
person_info = person()
person_info.display()

