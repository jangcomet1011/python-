def add_list(a, b):
    result = []
    len_a = len(a)
    len_b = len(b)

    if len_a > len_b:
        shorter_len = len_b
        for i in range(shorter_len):
            result.append(a[i] + b[i]) #2
        
        result = result + a[shorter_len:] 
    else:
        shorter_len = len_a
        for i in range(shorter_len):
            result.append(a[i] + b[i])
        
        result = result + b[shorter_len:]
        
    return result

print(add_list([1, 2, 3, 4], [1, 2]))
print(add_list([0, 1], [1, 2, 6, 7, 8]))