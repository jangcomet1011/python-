def hello(a, b) :
    for i in range(b):
        print(f"{a}")

a = input("반복 시킬 문자를 입력하세요 :")
b = int(input("반복시킬 횟수를 입력하세요 :"))

hello(a=a, b=b)