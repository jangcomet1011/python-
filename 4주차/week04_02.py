#week04_02.py
a = "abc"
b = list(a)
c = tuple(a)
print(b)
print(c)


t1 = tuple()
t2 = ()
t3 = (1)  #tuple아니 int
t4 = (1,) # 뒤에 , 를 붙여야 튜플로 인식한다
t5 = "1", 2, 2.3
t6 = ("1", 2, 2.3)

#수정,삭제,추가,삽입 모두 안돼!
#t6[0] = 1
#del t6[0]

a = t6 + t6 # ("1", 2, 2.3,"1", 2, 2.3)
b = t6 * 3  # ("1", 2, 2.3,"1", 2, 2.3,"1", 2, 2.3)
print(len(a), len(b)) #6 9
print(a, b)
print(a[-1]) #2.3
print(a[:3]) #("1", 2, 2.3) ()의 슬라이싱은 () # 슬라이싱: 0번부터 2번 인덱스까지 잘라내 '새로운' 튜플로 반환

def test():
    return 1,2,3,5,5 #tuple

a = test()
print(a)
b = list(a)
c = tuple(b)
