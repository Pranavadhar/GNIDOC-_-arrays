def union_intersection(arr1 , arr2):
    union = set(arr1) | set(arr2)
    intersection = set(arr1) & set(arr2)
    return list(union) , list(intersection)
arr1 = [1 ,2, 3 , 4, 5]
arr2 = [1 , 6 , 3 ,7 , 5]
print(union_intersection(arr1,arr2))