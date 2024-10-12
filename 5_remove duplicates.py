def remove_duplicates(Str):
    return "".join(sorted(set(str), key = str.index))
str = "hello"
print(remove_duplicates(str))