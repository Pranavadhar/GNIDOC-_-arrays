def max_product(arr):
    arr.sort()
    return max(arr[0] * arr[1] , arr[-1] * arr[-2])
arr = [-10 , -20 , 2 , 3]
print(max_product(arr))