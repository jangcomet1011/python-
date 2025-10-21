#week07_01.py
#힘수 응용2

def append_name(name, alist):
    if len(name) == 3:
        alist.append(name)

nlist = []
append_name("김인하", nlist)
append_name("이철", nlist)
append_name("박용현", nlist)
print(nlist)


def add(data, result):
    result += data #얘는 add함수 내부에서만 존재하는 지역변수라 전역변수에 영향을 끼칠 수 없다.
result = 0 #얘는 전역변수 

add(1, result)
add(2, result)
print(result)
print("*"*30)


#함수응용1

def findname_new(target, cmplist): 
    if isinstance(cmplist, list) and isinstance(target, str): #isinstance()함수는 타입을 검사하는 함수이 이 함수는 변수가
        if target in cmplist:                                #특정타입 변수인지 확인하는 역할을 한
            return True
        else :
            return False
print(findname_new([], "김인하")) #NONE
print(findname_new("김인하", [])) #Fasle



#sum([1,2]) #3
#sum(1,2) error sum()함수는 값을 한개만 받음 
def findname(target, cmplist):
    if target in cmplist: #cmplist 안에 target가 있는가?
        return True
    else :
        return False

names = ["김", "이", "박"]
result = findname("이", names)#true 리스트 ["김", "이", "박"] 안에는 "이"라는 요소가 포함되어 있으므로 조건은 **True**가 됩니다.
print(result)
result = findname(names, "이")#False 파이썬은 문자열 "이" 안에 리스트 ["김", "이", "박"]가 포함되어 있는지 확인하려고 합니다.
print(result) #문자열 안에는 문자만 포함될 수 있고, 리스트라는 데이터 구조가 통째로 들어갈 수는 없습니다. 따라서 조건은 **False**가 됩니다.



#전역/지역/변수

a = 1; b = 1; c = 1

def vartest1(a) :
 a = a + 1

def vartest2(b) :
    b = b + 1
    return b

def vartest3() :
    global c
    c = c + 1
    
vartest1(a)
b = vartest2(b)
vartest3()
print(a, b, c)





# **가변매개변수
def double_start(a, b, **kwargs): # **를 두개 붙이면 딕셔너리로 만든
    print(type(kwargs))
    for k, v in kwargs.items() :
        print(k, v)
    print(a, b)
    print(kwargs.get("loc", "-"))  #만약 .get()을 사용하지 않고 print(kwargs["loc"])처럼 대괄호([])를 사용하면, loc이라는 키가 없을 때 프로그램이 오류를 내고 멈춰버립니다.
    print(kwargs.get("field", "-"))

double_start("inha", "kim", field="cs", loc = "incheon")
double_start(b = "kim", a = "yonghyun", loc = "seoul")
double_start("jungsuk", "park", hobby = "song")




#가변매개변수
def calc(choice, *args): # 함수를 만들때 매개변수 이름앞에 * 를 붙이면 이 자리에 들어오는 모든 추가적인 인자들을 하나로 모아 튜플로 만들라는소리이
    print(type(args))    # calc("a", 1,2,3)함수를 호출하면 choice에 "a"가 들어가게 되고 *args 에는(1, 2, 3)이라는 튜플이 만들어져 들어간
    if choice.lower() == "a" :
        result = 0
        for i in args:
            result += i
    elif choice.lower() == "m":
        result = 1
        for i in args: result *= i
    else :
        result = None
    return result
a = calc("a", 1,2,3)
b = calc("m", 1,2,3)
c = calc("d", 1,2,3)
print(a,b,c)
#반환값
def add_and_mul1(a ,b):
    return a+b, a*b #2개를 전부 반환하는것 처럼 보이지만 튜플로 묶어서 한번에 반환시킴

def add_and_mul2(a, b):
    return a+b
    return a*b

print(add_and_mul1(3, 4))
print(add_and_mul2(3, 4))


#매개변수
#위치기반(1), 기본값(2), 키워드(3)
def multiply(a, b, c = 1, d = 1):
    return a*b*c*d

#m1 = multiply(1) 최소 2개는 집어넣어야함 
m2 = multiply(1,2)
m3 = multiply(1,2,3)
m4 = multiply(1,2,3,4)
#m5 = multiply(1,2,3,4,5) 변수가 너무 많음
m6 = multiply(a = 10, b = 2)
m7 = multiply(a = 10, b = 2, c = 2)
#m8 = multiply(a = 10, c = 2)
print(m2, m3, m4, m6, m7) #2 6 24 20 40

#기본 함수 만들기 및 호출하기
def add1(a, b) :
    return a + b

def add2() :
    return 1 + 2 

def add3(a, b):
    print(a + b) #3

def add4():
    print(1 + 2) #3

print(add1(1, 2)) #3
print(add2()) #3
print(add3(1, 2)) #NONE
print(add4()) #NONE
