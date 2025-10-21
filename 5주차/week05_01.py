#week05_01.py
#장은미
#(9)
score = int(input("점수:"))
if score >= 90:
    print("A")
elif score >= 80:
    print ("B")
else: 
    print("이건 좀...")
    if score >= 70: #중첩 if (nested if)
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
        

#(8)
score = int(input("점수:"))
if score >= 90:
    print("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
else:
    print ("F")


#(7)
socnum = input("주민등록번호:")

index = 7 if '-' in socnum else 6
gender = int(socnum[index]) % 2

if gender == 0:
    msg = "여성"
else:
    msg = "남성"

#(6)
socnum = input("주민등록번호:")
if '-' in socnum:
    index = 7
else:
    index = 6
gender = int(socnum[index]) % 2

if gender == 0:
    msg = "여성"
else:
    msg = "남성"
    
#(5)
socnum = input("주민등록번호:")
if '-' in socnum:
    gender = int(socnum[7]) % 2
else:
    gender = int(socnum[6]) % 2
    
if gender == 0:
    msg = "여성"
else:
    msg = "남성"
print(f"성별 : {msg}")




#(4)
socnum = input("주민등록번호:")
gender = int(socnum[7]) % 2
if gender == 0:
    msg = "여성"
if gender == 1:
    msg = "남성"
print(f"성별 : {msg}")



#(3)
#멤버십 연산자
names = ["jang", "song", "choi", "lee" ]
name = input("친구 이름:") # Jang

print(name in names) #F
print(name not in names) #T
print(name.lower() in names) #T
print(name.lower() not in names) #F




#(2)
car1 = "KiA"
car2 = "Kia"
print(car1 == car2) 
print(car1.lower() == car2.lower())
print(car1.upper() == car2.upper())



#(1)
toeic = int(input("TOEIC:"))
age = int(input("AGE:"))
temp = int(input("TEMPERATURE:"))

a = toeic >= 800 and age < 30
b = toeic >= 800 or age < 30
c = temp < 10 or temp > 28
d = age != 30 and toeic < 600
dd = not (age != 30 and toeic < 600)

height = int(input("height:"))
e = height >= 120 and height <= 160
e = 120 <= height <= 160 #***

print(a, b, c, d, dd, e)





