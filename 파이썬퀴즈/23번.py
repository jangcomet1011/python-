def search_index(a, b) :
    c = []
    for index, value in enumerate(a) :
        if value == b :
            c.append(index)
    return c




print(search_index([35,28,30,29,30],30))
print(search_index([35,28,30,29,30],31))