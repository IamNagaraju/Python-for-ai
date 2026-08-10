def anagram(str1, str2):
    obj = {}
    for char in str1:
        obj[char] = obj.get(char,0) + 1
    for char in str2:
        if char not in obj:
            return False
        obj[char] -= 1
        if obj[char] < 0:
            return False
    return True
print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))    # False