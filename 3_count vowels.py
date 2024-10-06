def count_vowel(str):
    vowels = "aeiouAEIOU"
    return sum(1 for char in str if char in vowels)
str = "HEISENBERG"
print(count_vowel(str))