def remove_Duplicates(arr):
    return ','.join(str(x) for x in sorted(set(arr), key = arr.index))
arr = [1,1,1,2,3,4,5,4,6]
print(remove_Duplicates(arr))