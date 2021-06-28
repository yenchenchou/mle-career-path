#953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create index for order to compare order
        # compare neighbor
        mapper = {s:i for i, s in enumerate(order)}
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]): return False
                if words[i][j] != words[i+1][j]:
                    if mapper[words[i][j]] > mapper[words[i+1][j]]:
                        return False
                    break
        return True  #O(mn), O(n)
