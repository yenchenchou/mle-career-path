# 1119. Remove Vowels from a String

class Solution:
    def removeVowels(self, s: str) -> str:
        newString = []
        removeSet = set("aeiou")
        for word in s:
            if word not in removeSet:
                newString.append(word)
        return "".join(newString)
    #O(n), O(n)