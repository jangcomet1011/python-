data1 = [1, 2, 3, 4, 5]
print(data1[0])
print(data1[-1])
print(data1[0] + data1[-1])
print(data1[:2])
print(data1[2:])
print(data1[2:-1])

data2 = [1, 2, 3, ["a", "b", "c"]]
print(data2[0], type(data2[0]))
print(data2[-1], type(data2[-1]))
print(data2[-1][-1], type(data2[-1][-1]))
print(data2[2:], type(data2[2:0]))
print(data2[3][1], type(data2[3][1]))
print(data2[3][:2], type(data2[3][:2]))
