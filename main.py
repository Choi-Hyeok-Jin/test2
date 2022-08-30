# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm

#order = {'최혁진': '비빔라면', '심정보': '매운라면'}
#print(order)
#order['최우현'] = '카레라면'
#print(order)
#order['심정보'] = '짜장라면'
#print(order)
#del order['최우현']
#print(order)


#def add_mul(num1, num2):
    #return num1 + num2, num1*num2

# print(add_mul(2,7))


#import random
#animals = ['최혁진', '최우현', '심정보']
#print(random.choice(animals))

#import random
#print(random.randint(1,10))

#import random
#청소정하기 = ['최혁진', '최우현', '심정보', '김도현', '김승연']
#print(random.sample(청소정하기, 2))

#import random
#청소정하기 = ['최혁진', '최우현', '심정보', '김도현', '김승연']
#청소당첨자 = random.sample(청소정하기, 3)
#print(청소당첨자, '청소하시기 바랍니다!')

#num = [1,2,3,4,5,6,7]
#for n in num:
    #print(n)
#print(num)

#for n in range(3):
    #print(n)


#clovers = ['클로버1', '클로버2', '클로버3']
#for ids in range(3):
    #print(clovers[ids])

#별성 = ['*','**','***']
#for star in range(3):
    #print(별성[star])

#total = 0
#card_nums = [1,3,6,7]
#for num in card_nums:
    #total = total + num
    #print(total/4)

#switch = '꺼짐'
#if switch == '켜짐':
    #print('조명이 커졌어요.')
#else:
    #print('조명이 꺼졌어요.')

#input_number = 0
#if input_number < 0:
    #absolute_number = input_number*-1
#else:
    #absolute_number = input_number
#print(absolute_number)

#print(abs(-678)) ## 절대값 내장함수
#total_price = 0
#menu = ['파스타', '스테이크', '리소또']
#for m in menu:
    #if m == '파스타':
        #total_price = total_price + 8000
    #elif m == '스테이크':
        #total_price = total_price + 12000
    #elif m == '리소또' :
        #total_price = total_price + 9000
#print('총 주문금액은', total_price, '입니다.')

#odd_nums = []
#for num in range(10):
    #if num % 2 == 1:
        #odd_nums.append(num)
#print(odd_nums)

#year = 2019
#if year % 400 == 0:
    #print(year, '년은 윤년입니다!')
#elif year % 4 and year % 100 != 0:
    #print(year, '년은 윤년입니다!')
#else:
    #print(year, '년은 윤년이 아닙니다.')

#count = 1
#while count < 4:
    #count = count + 1
    #print(count)

#count = 0
#while count <= 5:
    #if count % 2 != 0:
        #print(count)
    #count = count + 1

#n = 0
#while True:
    #print('안녕 거북이', n)
    #n = n + 1
    #if n == 3:
        #break

#while True:
    #print ('코딩 너무 좋아')
    #break

#price = 0
#price = int(input('가격을 입력하세요 (종료: -1): '))
#while price != -1:
    #if price > 10000:
        #print('너무 비싸요')
        #break
    #elif price > 5000:
        #print('괜찮은 가격이네요.')
        #break
    #elif price > 0:
        #print('정말 싸요.')
        #break

#while True:  ##찬우한테 물어보기
    #number = int(input('2 이상의 정수를 입력하세요 (종료 -1): '))
    #if number == -1:
        #break
    #count = 2
    #is_prime = True
    #while count < number:
        #if number % count == 0:
            #is_prime = False
            #break
        #count = count + 1
    #if is_prime:
        #print(number, '은(는) 소수입니다.')
    #else:
        #print(number, '은(는) 소수가 아닙니다.')

#num = 1,2,3
#for idx in range(3):
    #print(num[idx])

#attendence = 1,3,4,5
#최혁진, 심정보, 최우현, 김도현 = attendence
#print('심정보')


#alice = {'성별': '여', '나이': 13, '혈액형': 'ab'}
#alice['나이']=14
#print(alice['나이'])

#def welcome(name):
    #print(name, '이상한 나라에 오신 것을 환영합니다.')
#welcome('최혁진')

#def concat(str1, str2):
    #return str1 + str2
#print(concat('국민대 다니는', '최혁진입니다.')

#def judge_cards(name, num):
    #for n in range(num):
        #print(name, n+1, '유죄!')
#judge_cards('최혁진', 2)

#import random
#clovers = ['클로버1', '클로버2', '클로버3']
#print(random.sample(clovers, 2))

#import random
#print(random.randrange(1,4))

# f문자열 포매팅
# 파이썬 3.6부터는 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.
#name = '최혁진'
#age = '25'
#a = f"나의 이름은 {name}이며, 나이는 {age} 입니다. "
#print(a)

# %간격. 소수점 남기는 자리 수f
# a = "%0.4f" % 3.421421421
# print(a)

# 문자열 자료형과 관련된 내장함수
# 함수란? 어떤 특정한 일을 하는 명령어들을 묶어 놓은 것
# count = 문자 개수 세기 함수
# find, index = 위치 알려주기 함수, 문자열에 제일 처음 나온 위치만 알려줌.
# a = "hobby"
# a.count('b')
# print(a.count('b'))
#
# # join = 문자열 삽입 함수
# a = ",".join("abcd")
# print(a)
#
# # upper = 소문자를 대문자로 바꾸기
# # lower = 대문자를 소문자로 바꾸기
# a = 'hi'
# b = 'HI'
# print(b.lower())
#
# # strip = 공백지우기
# a = '   ji   '
# print(a.strip())
#
# # replace = 문자열 바꾸기
# a = "life is too short"
# print(a.replace("life", "youre leg"))

# split = 문자열 나누기, 문자열 자료형 있으면 띄어쓰기 기준으로 잘라서 리스트로 만들기
# a = "life is too short"
# print(a.split())
#
# # 리스트 = 변수 여러 개를 묶는 역할, 하나의 변수에 여러 개의 값을 관리할 때 사용합니다.
# a = [1,2,'int', '최혁진', ['심정보', 'manse samdori']]
# print(a[4][0]) # 리스트의 인덱싱, 리스트 안에 리스트를 소환할 때!
#
# # 리스트 슬라이싱 & 리스트 더하기 % 곱하기
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print(a[0:3])
# print(a*2)
# print(a+b)
#
# # 리스트 하나의 값 or 여러개의 값을 수정하기 or 삭제하기
# a = ['박주하', '잠수', '문재성']
# a[0] = '한재성'
# a[0:2] = ['김정현', 'stopmotion man']
# print(a)
#
# # 리스트 값 삭제하기-1
# a = ['박주하', '잠수', '문재성']
# a[0:2] = []
# print(a)
#
# 리스트 값 삭제하기-2
name = ['최혁진', '김도현', '김승연']
del name[0]
print(name)0



