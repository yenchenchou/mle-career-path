# 973. K Closest Points to Origin
# Solution1:
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get all the distance and store in a dic with dis will be the key and val will be the index pointing to the list
        # sort the distance list and count according to k
        dic, res = {}, []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            dic[i] = distance
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=False)
        for i in range(k):
            index = dic[i][0]
            res.append(points[index])
        return res  # O(nlogn), O(n)


# Solution 1.2
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]  # O(nlogn), O(n)
