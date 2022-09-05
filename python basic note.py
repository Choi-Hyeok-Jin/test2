# # print("hello")
# # a = [1,2,3,4,5,6]
# # del a[0]
# # print(a[0:3])
#
# # a = [1,2,3,4,4]
# # a.extend([5,6])
# # print(a)
#
# # a = ','
# # print(a.join('abcd'))
# #
# # a = 'hi'
# # print(a.upper())
#
#
# # name = '최혁진 심정보 최우현 김승연 김도현'
# # print(name.find('최'))
#
# # a = '%s' %' 파이썬어린이'
# # print(a*2)
#
# ti = (1,2,'a','b')
# del ti[1]

# a = {'1번': '최혁진', '2번': '심정보', '3번':'최우현'}
# # print(a.keys())
# # print(a.values())
# # print(a.items())
# # print('3번' in a)

# 집합 set 만들기! = 중복되는 값 제거하기!
# s1 =set([1,2,3,4,4])
# s2 = {1,2,3,3,5}
# print(list(s2)) # set으로 중복되는 값을 제거하고, 리스트 함수로 리스트 만들기

# 집합 set 문자열 적용 시, 각각의 원소(글자 하나)로 나누어지며, 중복되는 글자는 삭제된다.
# s1 = set('hello') # 집합은 순서없고, 중복되지 않는다
# print(s1)

# 집합 set 으로 교집합, 합집합, 차집합, 추가, '여러 개' 추가, 제거 만들기
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# # print(s1&s2)
# # print(s1.intersection(s2))
# # print(s1|s2)
# # print(s1.union(s2))
# # print(s1-s2)
# # print(s1.difference(s2))
# s1.add(7)
# s1.update([8,9,10])
# print(s1)
# s1.remove(10)
# print(s1)
#
# #bool 리스트에 변수가 있으면 참, 없으면 거짓으로 출력!
# a = [1,2,3,4,5]
# while a:
#     a.pop()
#     print(a)

# 변수에 대한 구체적인 설명
# a= [1,2,3]
# 'a'라는 변수 안에 리스트로 둘러싸인 '1','2','3'이라는 객체(값)=인덱스=주소가 존재하는 것!

# # a의 주소를 b가 고스란히 물려받다. * 변수의 주소를 받게되면, 값도 연동되어 변경될 수 있다.
# a= [1,2,3]
# b = a
# a[1] = 4
# print(id(a)) # a의 주소값 확인
# print(id(b)) # b의 주소값 확인
# print(a is b) # a와 b가 같은 주소를 갖고 있는 가에 대한 함수
#
# # a의 주소와 b의 주소를 다르게 하는 방법 * 슬라이싱하기 *값만 복사하기
# a= [1,2,3]
# b = a[:] #처음부터 끝까지 슬라이싱 하기!
# a[1] = 4
# print(a) # a의 주소값 확인
# print(b) # b의 주소값 확인
# print(a is b) # a와 b가 같은 주소를 갖고 있는 가를 확인하는 함수

# # a의 주소와 b의 주소를 다르게 하는 방법 * import copy
# from copy import copy # 파이썬 밖의 존재하는 라이브러리를 가져오기
# a= [1,2,3]
# b = copy(a)
# a[1] = 4
# print(a) # a의 주소값 확인
# print(b) # b의 주소값 확인
# print(a is b) # a와 b가 같은 주소를 갖고 있는 가를 확인하는 함수

# 리스트, 튜플을 이용해서 각각 a,b 변수 만들기

# (a, b) = ('김덕배', '마리노') # 변수에 튜플을 넣어도 되고, 안 넣어도 됨!
# print(a)
# print(b)

# a,b 변수의 값을 교체하기
# a, b = ('김덕배', '마리노')
# a, b = b,a  -> 방법 1
# tmp = b -> 방법 2
# b = a
# a = tmp
# print(a)

# 제어문 = 조건문(if), 반복문(for, while)


# 연산자를 이용한 if문
# money = 2000
# card = 1 # 파이썬에서 '1' = 참, '0'은 거짓에 해당한다.
# if money >= 3000 or card:  #카드가 1이므로 true로 적용됨!
#     #print('택시타고 가라')
#     pass # 그냥 통과하라는 함수
# else:
#     print('걸어서 가라')

# # elif 문
# pocket = ['paper', 'cellphone']
# card = 1
# if 'money' in pocket:
#     pass
# elif card:
#     print('택시타고 가라')
# else:
#     print('걸어가라')

# 한 줄 조건부 표현식 만들기
# score = 70
# if score >= 60:
#     meessage = 'success'
# else:
#     meessage = 'fail'
# print(meessage)
# score = 70
# message = 'success' if score >= 60 else 'fail'
# # 3항 연산자? = if문을 간단하게 한 줄로 쓰기
# # (조건문이 참인 경우) if(조건문) else (조건문이 거짓인 경우)
# print(message)

#반복문(while)

# treehit = 0
# while treehit < 10:
#     treehit = treehit + 1
#     print("나무를 %d번 찍었습니다." % treehit)
#     if treehit == 10:
#        print("나무가 넘어갑니다.")
#
# while문 break
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# while문 continue

# a = 0
# while a < 10:
#     a= a+1
#     if a% 2 == 0:
#         continue
#     print(a)

# while문 무한반복
# while True:
#     print("안녕하세요")
#     break

# for문의 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#    수행할 문자1
#    수행할 문자2

# for문 튜플형
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     # print(first)
#     # print(last)
#     print(first + last)

# # for문 응용
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# for문 continue

# # if-for-continue 문
# marks = [90, 25, 77, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60:
#         break #continue # 다시 처음으로 돌아간다!
#     print("%d번 학생 축하합니다. 합격입니다." %number)

## for-range 문

# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

# ## double for 문
# for i in range(2,10):
#     for j in range (1,10):
#         print(i*j, end="")
#         # end= " "// print 함수의 option, 한줄씩 띄지 않고, 마지막에 end가 이어져서 나옴
#     print('')
#앞의 예제에서 print(i*j, end="")와 같이 매개변수 end를 넣어 준 이유는 해당 결과값을
#출력할 때 다음 줄로 넘기지 않고, 그 줄에 계속해서 출력하기 위해서이다. 그 다음에 이어지는
#print('')는 2단, 3단 등을 구분하기 위해 두 번째 for문이 끝나면 결과값을 다음 줄부터
# 출력하게 해주는 문장이다!!

# 리스트 내포 사용하기
# result = [x * y for x in range(2,10) for y in range(1,10)]
# print(result)

# 리스트 내포 다른 표현
# result = []
# for x in range(2,10):
#     for y in range(1,10):
#         result.append(x*y)
# print(result)
# 파이썬 함수의 구조
# def 함수명(매겨변수): 매개변수는 input
# <수행할 문장1>
# <수행할 문장2>  # 1,2는 함수f
# ruturn 리턴 값  # output f(x)

# 함수문의 예제
# def sum (a,b):
#     return a+b
# print(sum(1,2))
#
# # 입력값이 없어도 출력가능
# def say():
#     return 'hi'
# print(say())

# # 입력값은 있지만, 출력값(return)이 없어도 출력가능
# def sum(a,b):
#     print("%d, %d의 합은 %d입니다." % (a,b,a+b))
# print(sum(1,2))

## append 함수는 출력값이 없고, pop 함수는 출력값이 있다.
# mylist = [1,2,3]
# print(mylist.append(4))
#
# mylist = [1,2,3]
# print(mylist.pop())
# print(mylist.pop())

# *args : 입력값 개수의 제한받지 않고, 무한대로 입력가능
# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     return sum
# print(sum_many(1,2,3,4,5,6,7))


# #kwarges.key = ['최혁진', '심정보', '최우현']
# def print_kwarges(**kwargs):
#     for k in kwargs.key():
#         if (k == "name"):
#             print("당신의 이름은 :" + k)
# print(print_kwarges(name="int 조수"))
# 함수의 결과 값은 언제나 튜플 형태로 하나이다.
# def add_and_mul(a,b):
#     return a*b, a+b, a-b
# print(add_and_mul  (1,2) [0])

#매개변수 초기값 미리 설정하기
# def say_myself(name,old, man=False):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %s살입니다." %old)
#     if man:
#         print("남자입니다.")
#     else:
#         print('여자입니다.')
# print(say_myself("최혁진", 25))

## 함수 안에서 선언한 변수의 효력 범위

# 1) 지역변수
# a=1
# def vartest(a):
#     a = a +1
#     return a
#
# print(vartest(2))
# print(a)

# 2) 지역함수가 범위 밖에 'a' 변수에게 영향을 주기
# a=3
# def vartest(a):
#     a = a + 1
#     return a
# a = vartest(a)
# print(a)

# lambda 함수 사용하기! 함수를 한 줄로 축약해서 표헌하기
# def add(a,b)
#     return a+b
# add = lambda a,b: a+b
# print(add(1,2))
## -> 리스트 안에 def 함수는 못 넣지만, 람다 함수는 사용가능!!
# mylist = [lambda a,b: a+b, lambda a,b: a*b]
# print(mylist[1](3,4))

# 사용자 정의 함수 input
# number = input("당신의 이름을 입력해주세요: ")
# print(number)

# print end('')
# for i in range(10):
#     print(i, end='번')

# # 파일 읽고 쓰기: 파일 생성하고 쓰기 모드
# f = open("새파일.txt", 'w', encoding = "UTF-8")
# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()
#
# # 파일 읽고 쓰기: 파일 읽기 모드
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# while True:
#     line = f.readline()
#     if not line: # 한줄씩 모두 읽고 싶을 때!
#         break
#     print(line)
# f.close()
#
# # 파일 읽고 쓰기: 파일 읽기 모드 - (1)
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()
# #
# # 파일 읽고 쓰기: 파일 읽기 모드 - (1) * 한줄씩 띄우기 없애기
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line, end="")
# f.close()
#
# # 파일 읽고 쓰기: 파일 읽기 모드 - (1) * 한줄씩 띄우기 없애기
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip('\n'))
# f.close()
#
# # 파일 읽고 쓰기: 파일 읽기 모드 - (1) * 한줄씩 띄우기 없애고, 한 줄로 출력하기
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip('\n'), end=(''))
# f.close()

# # read() 함수 이용해서 통째로 읽기
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# data = f.read()
# print(data)
# f.close()

# # # 파일 읽고 쓰기: 파일 추가하기 - (2)
# f = open("새파일.txt", 'w', encoding = "UTF-8")
# for i in range(1,11):
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()
#
# f = open("새파일.txt", 'a', encoding = "UTF-8")
# for i in range(11,21):
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()
#
# # f = open("새파일.txt", 'r', encoding = "UTF-8")
# # data = f.read()
# # print(data)
# # f.close()
#
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip('\n'))
# f.close()

## 파일생성 with 쓰기 >> f.close()문을 안써도 됨!
# with open('foot.txt', 'w') as f:
#    f.write("life is too short, you need python")

#class = 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
# class Fourcal:
#     def __init__(self, first, second): #먼저 실행하는 생성자
#        self.first = first
#        self.second = second
#     def setdata(self, first, second): # a= self
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def pow(self):
#         result = self.first ** self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# a = Fourcal(1,2)  # 클래스의 객체(인스턴스) = a.b
# b = Fourcal(3,4)
# print(b.add())
# b = Fourcal()
# a.setdata(2,4) # 객체 a의 객체변수 2,4
# b.setdata(3,7) # 객체 b의 객체변수 3,7
# print(b.add())
# print(b.first)
# print(b.second)

# 클래스의 상속 = 부모의 클래스를 자식이 물려받는다.
# class Morefourcal(Fourcal):
#     def mul(self):
#         result = self.first * self.second
#         return result

# a = Morefourcal(4,2)
# print(a.add())
# print(a.pow())

# 메서드 오버라이딩 = 부모의 함수를 덮어쓴다.
# class Safefourcal(Fourcal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first ** self.second
# a = Safefourcal(4,2)
# print(a.div())
#
# 클래스 변수 (종속적) vs. 클래스 객체 (독립적)
# class Family:
#     lastname = '김'
# print(Family.lastname)
# Family.lastname = '박'
# print(Family.lastname)
# a = Family()
# b = Family()
# print(a.lastname)
# print(b.lastname)

## 파이썬 모듈 생성하고, 불러오기 사용법
# import mod1
# print(mod1.add(1,2))
# from mod1 import add
# print(add(1,2))

# 모듈- 다른 경로에 있는 파이썬 모듈 불러오기
# import sys
# sys.path.append("C:/Users/user/PycharmProjects/test2/subfolder")
# import mod1
# print(mod1.add())

# '패키지'란 여러 개의 모듈을 모아놓은 것. - mod3 불러오기
# from subfolder.test.echo import mod3 as a
# # 파일들 명 사이의 '.' = '속한다' 라는 표현임!
# # 'as'는 mod3를 'a'라고 간단하게 지칭할 때 사용하는 표현임
# print(a.div(9,3))

## 전체 모듈을 사용하려 할 때, 폴더 안에 init 파일을 꼭 만들어줄 것!!
# from subfolder import *
# mod1
# print(mod2.mul(2,4))

# 예외처리 try-except로 에러구문 처리하기!
# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# print("최혁진 안녕하세요.")

# try:
#     a = [1.2]
#     print(a[3])
#     4 / 0
#
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try:
#     f = open("나 없는 파일", 'r')
# except FileNotFoundError:
#     pass
#
# print('최혁진')

# 내장함수 filter
# def positive(x):
#     return x > 0
#
# a = list(filter(positive, [1,-3,4,0,-2,6]))
# print(a)

# 내장함수 map = 각 요소가 수행한 결과를 돌려줌!

# def two_times(numberlist):
#     result = []
#     for number in numberlist:
#         result.append(number*2)
#     return result
# result = two_times([1,2,3,4])
# print(result)
# def two_times(x):
#     return x*2
# a = list(map(two_times, [1,2,3,4]))
# print(a)

# b= list(map(lambda a: a*2, [1,2,3,4]))
# print(b)

#내장함수 zip
# print(list(zip([1,2,3],[4,5,6],[7,8,9])))

# 외장함수 = 라이버르리 함수, import 해서 쓰는 것!
# argv_test.py

# import random
# lotto = sorted(random.sample(range(1,46),6))
# print(lotto)
#
# f = open("새파일.txt", 'r', encoding = "UTF-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# import pickle 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있는 함수다.
#
# name ='최혁진'
# age = 25
# address = '서울시 성북구 정릉동'
# scores = {'korean': 90, 'english': 95, 'mathmatics': 85, 'science': 82}
#
# with open ('새파일.txt', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)

# import pickle
#
# with open ('새파일.txt', 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     address = pickle.load(file)
#     scores = pickle.load(file)
#
# print(name)
# print(age)
# print(address)
# print(scores)