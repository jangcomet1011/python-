def add_dict(a,b,c) :
    if b in a :
        return False
    else :
        a[b] = c #이과정에서 scores에 {"park" : 100}이 추가됨
        return True



scores = {"kim":95,"lee":65}
if add_dict(scores, "park", 100) :
    print("입력완료")
else : 
    print("동일학생 있음")

if add_dict(scores, "kim", 100) :
    print("입력완료")
else : 
    print("동일학생 있음")
