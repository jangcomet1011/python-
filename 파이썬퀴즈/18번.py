def remove_value(a , b) :
    del a[b-1]
    return a


numbers = [1,2,3,4,5]
result = remove_value(numbers,2)
print(result)