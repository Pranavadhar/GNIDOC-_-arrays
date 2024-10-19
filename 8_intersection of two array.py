def intersection(arrone , arrtwo):
    return list(set(arrone) & set(arrtwo))
arrone = [1 , 3, 4,5,9,6,2]
arrtwo = [ 1 ,3, 0 ,4, 7] 
print(intersection(arrone , arrtwo))