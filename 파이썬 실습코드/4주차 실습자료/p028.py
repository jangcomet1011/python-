cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
print(cars)

# 오름차순(정방향,asc)으로 정렬
cars.sort()
print(cars)

# 내림차순(역방향,desc)으로 정렬
cars.sort(reverse=True)
print(cars)
print("-" * 60)
cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]

# 오름차순(정방향,asc)으로 정렬
cars_copy = sorted(cars)
print(cars_copy)

# 내림차순(역방향,desc)으로 정렬
cars_copy = sorted(cars, reverse=True)
print(cars_copy)
print(cars)

print("-" * 60)
cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
cars.reverse()
print(cars)

print("-" * 60)
# 원본 손상없이 reverse()를 하려면?
cars = ["audi", "tesla", "benz", "kia", "lincoln", "hyundai"]
cars_copy = cars[:]  # 복사
cars_copy.reverse()
print(cars)
print(cars_copy)
