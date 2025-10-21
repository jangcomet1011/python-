def merge_list(a, b) :
    sum = a + b # [1,2,3,4,1,2,5]
    sum2 = set(sum) #{2,3,1,4,5} set()은 순서가 존재x
    sum3 = sorted(sum2) #sorted함수는 전달받은 데이터를 오름차순으로 정리해주는 내장함수 set()이였던 자료형이 오름차순으로 정렬되며 []리스트 형식으로 바뀐다
    return sum3 

print(merge_list([1,2,3,4],[1,2,5]))
print(merge_list([0,1,10],[1,2,6,7,8]))