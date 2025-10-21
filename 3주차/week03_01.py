#week03_01.py
a = ""              #빈 문자열
b = "I like Python"
c = " "             #공백 문자열

print(len(a))
print(len(b))
print(len(c))



print("#" * 30)

t1 = 1
t2 = "1"
a = t1 + t1  
b = t2 + t2
c = str(t1) + t2 #==b 
d = t1 + int(t2) #==a
print(a, b, c, d)

print("*" * 10)

a = "in'h'a \nuniv"
b = 'in"h"a \nuniv'
c = """inha
univ"""
d = """inha
       univ"""
print(a)
print(b)
print(c)
print(d)
