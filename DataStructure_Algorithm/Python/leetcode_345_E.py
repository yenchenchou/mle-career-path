# 345. Reverse Vowels of a String
# easiest problem 1119

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s)-1
        
        while left <= right:
            if s[left] in vowel and s[right] in vowel:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowel:
                left += 1
            if s[right] not in vowel:
                right -= 1
        return "".join(s) #a, n, ai, an, aen
    #O(n), O(n)