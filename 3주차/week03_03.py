#week03_03.py
age = 21
name = "정석"
temp = 31.5

# (3)f-string
a = f"내 이름{name:>10}"                              
b = f"이름:{name:<10} 나이:{age:^10}"   
c = f"현재 온도 {temp:0.3f}"
d = f"이름:{name} 내년나이:{age+1}"
print(a);print(b);print(c);print(d);

print("#" * 30)

# (2)str.format() 메소드
a = "내 이름 {0:>10}".format(name)
b = "이름:{0:<10} 나이:{1:^10}".format(name,age)
c = "현재 온도 {0:0.2f}".format(temp)
print(a); print(b); print(c)

print("#" * 30)

# (1)%-format
a = "내 이름 %10s" % name
b = "이름:%-10s 나이:%d" % (name, age)
c = "현재 온도 %0.1f" % (temp)
print(a); print(b); print(c)
