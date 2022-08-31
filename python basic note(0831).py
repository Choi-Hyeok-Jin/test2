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