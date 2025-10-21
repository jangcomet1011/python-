
#printf()와 유사한 함수 - print()
#마지막에 반드시 줄을 바꾼다!
#print()역할 -> 문자열을 화면에 출력!

print() #줄만 바꿈.
print(1) #정수 -> "1" 변경 후 출력 
print(1.1) #실수 -> "1.1" 변경 후 출력 
print([1,2,3]) #리스트 -> "[1,2,3]" 변경 후 출력 
print("123")
print("1" "2" "3") # "123"
print("1","2","3") # "1 2 3"
print("1"+"2"+"3") # "123" 문자열연결연산자로 결합 후 print로 전달 

#print()의 마지막을 변경하려면
#end옵션을 사용한다.
#기본 end="\n"
print("1", end="")
print("2", end="qq")
print("3", end="\t")
print("4", end="")





#scanf()와 유사한 함수 - input()

#int a;
#printf("나이를 입력하세요.")
#scanf("%d", &a);
#printf("%d", a); 

a = input("나이를 입력하세요.")
print(a)

print(type(a))
#print("내년 나이" , a + 1)
#파이썬은 문자열 + 숫자 형식 지원하지 않음.

print("내년 나이" , a + "1")
# + 문자열 연결 연산자 201

print("내년 나이" , int(a) + 1)
# + 산술 연산자        21



#한줄 주석 //
"""
/*
여러줄주석인 척하는 문자열...
*/
"""

if True:
    print("장")
    print("은")
    print("미")
    
'''
if(1)
{
    printf("장\n");
    printf("은\n");
    printf("미\n");
}
'''    








