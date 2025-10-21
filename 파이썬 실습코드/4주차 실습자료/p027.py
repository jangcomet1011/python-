motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# 변경하기
motorcycles[0] = "bmw"
print(motorcycles)

# 추가하기
motorcycles.append("vespa")
print(motorcycles)

# 삽입하기
motorcycles.insert(0, "daelim")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "bmw", "ducati", "vespa", "kia"]

del motorcycles[2]
print(motorcycles)  # 인덱싱

del motorcycles[-1]  # 인덱싱
print(motorcycles)

del motorcycles[:2]  # 슬라이싱 일부
print(motorcycles)

del motorcycles[:]  # 슬라이싱 전체, motorcycles.clear() 동일
print(motorcycles)

del motorcycles[10]  # index out of range
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "bmw", "ducati", "vespa"]

popdata = motorcycles.pop()
print(motorcycles)
print(popdata)

popdata = motorcycles.pop()
print(motorcycles)
print(popdata)

popdata = motorcycles.pop(2)
print(motorcycles)
print(popdata)

motorcycles.remove("yamaha")
print(motorcycles)

popdata = motorcycles.pop(10)  # index out of range
motorcycles.remove("YAMAHA")  # x not in list
