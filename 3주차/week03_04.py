#week03_04.py
test1 = "  JMT University   "

#str.split()의 반환형 : list
#공백 문자를 기준으로 분리
print(test1.split())
#조건 문자를 기준으로 분기
print(test1.split("i"))
print("*" * 30)
#str.replace() 원 문자열을 손상시키지 못함.
#              신규 문자열 생성
#문자열은 불변데이터.
print(test1.replace("University", "High School"))      #첫번째는 바꿀대상 두번째는 바꿀 내용이다 그래서 출력값은
print(test1)                                           # JMT High School 이다


print("|" + test1.strip()  + "|")  #양쪽공백 제거
print("|" + test1.lstrip() + "|")  #왼쪽공백 제거
print("|" + test1.rstrip() + "|")  #오른쪽공백 제거


print("*" * 30)

test2 = "iam a BOY."

print(test2.upper())
print(test2.lower())
print(test2.title()) #각  단어 첫글자만 대문자로 
print(test2.capitalize()) #문장의 첫글자만 대문자로 

print("*" * 30) 
print("/".join(test2))
print("*" * 30) 

print(test2.find("am"))
print(test2.find("q"))
print(test2.index("am"))
#print(test2.index("q")) 인덱스는 없으면 -1 출력 대신에 오류를 일으킨다

print("*" * 30)



print(len(test2))       #함수 len()
print(test2.count("a")) #메소드 count()

#형태적 으로 분석
#len(a)  #(모두의) 함수
#a.len() #(누군가의/누가가만 호출) 메소드 







