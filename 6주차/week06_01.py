#week06_01.py
#jang eunmee

students = []
titles = ["국어", "영어", "수학"]

number = int(input("인원:"))
for n in range(1, number+1):
    print(f"{n} 학생:")
    scores = []
    for t in titles:
        score = float(input(f"{t}:"))
        scores.append(score)
    students.append(scores)
#students = [[10,20,30],[1,2,3]]

for v in enumerate(students):
    print(v) #tuple
    print(v[0], v[1]) #v[1]:list
print("*" * 30)
for i, v in enumerate(students):
    print(i, v) #v:list
print("*" * 30)
for i, v in enumerate(students):
    print(f"{i+1}:")
    for j, score in enumerate(v):
        print(f"{titles[j]}:{score}")
    


    

values = ['1', '2', '3']
# 위 values의 데이터를 모두 정수로 변환한
# 새로운 리스트를 만들어보세요.

#반복문
values_new = []
for v in values:
    values_new.append(int(v))

#리스트내포
values_new = [int(v) for v in values]

#map()
values_new = list(map(int, values))





    

