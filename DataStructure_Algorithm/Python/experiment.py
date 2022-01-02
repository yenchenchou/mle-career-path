from typing import List
class Solution:
    def string_encoding(self, string: str) -> List[List[int]]:
        """
        1. Clarify the question
            -> need to do counting
            -> but what about the char has only one count and causing the need for extra space
        2. Draw an example
                a a a a b b b c c c c c e
                a 4 b 3 c 5 e c c c c c e
                                         f
                              s
                cnt=5
                a4b3c5e1

                a4bc4e

        3. Two scans:
            -> left to right scan, we only deal with patterns that make the encoding shorter <char><count>. 
                -> Thats is to say leave single letter unchanged and count how many single chat for 
                -> preparing extra space
                    -> fast, slow pointer
                        -> slow: all the chars on the left side (exclude slow) is the intermediate 
                        -> fast: the pointer do the scanning
            -> right to left scan to perform the pre-calculation based on the counter in step1
        """
        # corner case
        # bb3c5e1
        # l
        #f
        if not string: return ""
        string = list(string)
        fast = self.pre_encode(string)
        slow = len(string) - 1
        while fast > 0:
            if fast -1 > 0 and string[fast].isdigit() and string[fast-1].isalpha():
                string[slow] = string[fast]
                string[slow-1] = string[fast-1]
                slow -= 2
                fast -= 2
            elif fast == 0:
                string[slow] = string[fast]
                slow -= 1
                fast -= 1
            else:
                string[slow] = 1
                slow -= 1
                string[slow] = string[fast]
                slow -= 1
                fast -= 1
        return string

    def pre_encode(self, string):
        # left to right
        fast, slow, extra = 0 ,0, 0
        while fast < len(string):
            cnt = 0
            string[slow] = string[fast]
            while fast < len(string) and string[slow] == string[fast]:
                fast += 1
                cnt += 1
            slow += 1
            if cnt > 1:
                string[slow] = str(cnt)
                slow += 1
            else:
                extra += 1
        string.extend([None]*extra*(2-1))
        return len(string) - slow + 1
            

sol = Solution() 
print(sol.string_encoding("aaaabbbccccce"))