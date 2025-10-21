#week05_02.py
#장은미

#(8)
scores = [10, 20, 15]
offset = []
for score in scores:
    if score >= 15:
        offset.append(score + 2)

offset = []
#offset = [for score in scores] 뭐가 오류난거지?
offset = [score for score in scores]
offset = [score + 2 for score in scores]
offset = [score + 2 for score in scores if score >= 15]
        

        

#(7)
for i in range(5):
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
    print(f"{i+1}:{scores[i]}")




#(6)
scores = [100, 90, 75]
summary = 0
for score in scores:
    summary += score

avg1 = summary / len(scores)
avg2 = sum(scores) / len(scores)
print(avg1, avg2)





#(5)
name = ['inha', 'dongyang']
for n in name:
    print(n)

#(4)
name = "장은미"
for n in name:
    print(n)   
    #장
    #은
    #미
    

#(3)
while True:
    name = input("이름:").strip().lower() #.strip()함수는 공백제거거
    if name == "quit":
        break
        
    print(name)
    
#(2)
name = ""
while name != "quit":
    name = input("이름:").strip().lower()
    print(name)


#(1)
i = 0            #초기식
while i < 10:    #조건식
    i += 1       #증감식, i++ , ++i은 안됨
    print(f"{i}번")
    


    
