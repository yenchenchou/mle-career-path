# 1086. High Five

# Solution1: Use sort and save the value in dic
# then only get the top 5 elements for each dictionary
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items = sorted(items, reverse=True)
        dic = {}
        res = []
        for item in items:
            id, score = item[0], item[1]
            if id not in dic:
                dic[id] = [score]
            else:
                dic[id].append(score)

        for key, val in dic.items():
            ans = [key, sum(val[:5]) // 5]
            res.append(ans)

        return res[::-1]

    # O(nlogn+n), O(n)

# Solution2: Use sort and save the value in dic