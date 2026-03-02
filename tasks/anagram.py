def anagram(str1, str2):
    if sorted("".join(str1.split())) == sorted("".join(str2.split())):
        return True
    else:
        return False
print(anagram("the see", "the eyes"))

a, b = 0, 1
print(f"{a}{b}")