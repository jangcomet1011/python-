t = (1, 2, "a", "b")
a = t[0]

t[0] = 3
del t[0]
t.remove(1)
t.pop()
t.append(3)
del t[0]


titles = ("국어", "영어", "수학")
print(titles[0])
print(titles[1])
print(titles[2])

for title in titles:
    print(title)

a, b = 1, 2
print(a, b)
a, b, c = (1, 2, 3)
print(a, b, c)
a, b = (1, 2, 3)  # 개수가 일치하지 않는다.
print(a, b)
