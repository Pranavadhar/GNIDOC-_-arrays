def seclargeele(arr):
    arr.sort()
    return arr[-2]

arr = [1,2,3,4,5]
print(seclargeele(arr))