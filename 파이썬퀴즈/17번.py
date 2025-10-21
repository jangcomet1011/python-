def list_avg(a) :
    b = sum(a)
    avg = b / len(a)
    return avg



numbers = [1,2,3,4,5,6,7,8,9,10]
result = list_avg(numbers)
print(result)