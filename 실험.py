"""for i in range(5):
    print(i, end="/")
print()
print("*"*30)
for i in range(1, 5):
    print(i, end="/")
print()
print("*"*30)
for i in range(1, 5, 2):
    print(i, end="/")
print()
print("*"*30)
for i in range(5, 0, -1):
    print(i, end="/")
print()
print("*"*30)
scores = [10,20,15]
for i in range(len(scores)):
    print(f"{i+1}:{scores[i]}") """


print("-------기본 dict 사용법--------")    
info = {} #info = dict()
info["n"] = "김인하" #(append) str:str
info["a"] = 23       #(append) str:int
info["h"] = 163.2    #(append) str:float
info[1] = 'One'      #(append) int:str
print(info)

info["h"] = 173.2     #(update) 
print(info)

del info["h"]          #(delete)
print(info)

#print(info['h']) - KeyError

if 'h' in info: #멤버십 연산자 이용해 key 유무 확인
    print(info['h'])
else:
    print("키 미등록")

search = info.get('h')#dict.get()메소드 이용해 값 찾기
if search:
    print(search)
else: # search => None => False
    print("키 미등록")

#dict.get()의 두번째 인자에 None의 대체값 넣기.
print(f"키:{info.get('h', '-')} cm")

