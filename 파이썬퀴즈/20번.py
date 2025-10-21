def get_students(a) :
    return a.keys()






scores = {"kim" : 95, "lee" : 65}
students = get_students(scores)

if len(students) > 0:
    students = ",".join(students)
    print(students)
else : 
    print("학생이 없음음")