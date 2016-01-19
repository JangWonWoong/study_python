a = 5
b = 6

import math

a_huge_number = math.factorial(1024)

a2 = str(a)
b2 = str(b)
print(a2 + b2)
print(int(a2) + int(b2))
print(float(a) + float(b))

username = "jang won woong"
print(username.title()) # 이름 쓸때
print(username.startswith('j'))
print(username.upper())
print(username.lower())

#non type
empty_string = ''

# Flase
print(empty_string is None) # 메모리에 존재 하지 않는 것을 체크

# True
print(len(empty_string) == 0)

def none_func():
    pass    # return 값이 없으면 아무것도 하지 않는 코드를 입력

# False
print(none_func is None)    # 함수 자체는 존재 하기 때문에 Not None

# True
print(none_func() is None)  # return 값은 존재 안하기 떄문에 None

family = ['mother','father','gentlman','sexy lady']
print(len(family))

print(family[3])
family.remove('mother')
print(family)

num = 1
while num <= 100:
    print(num)
    num += 1

for x in family:
    print('%s %s' % (x, len(x)))