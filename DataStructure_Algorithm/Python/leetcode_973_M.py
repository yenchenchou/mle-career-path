# 973. K Closest Points to Origin
# Solution1: hash map
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get all the distance and store in a dic with dis will be the key and val will be the index pointing to the list
        # sort the distance list and count according to k
        dic, res = {}, []
        for i in range(len(points)):
            distance = (points[i][0] ** 2 + points[i][1] ** 2) ** 1 / 2
            dic[i] = distance
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=False)
        print(dic)
        for i in range(k):
            index = dic[i][0]
            res.append(points[index])
        return res  # O(nlog), O(n)


# Solution1: max heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get all the distance and store in a dic with dis will be the key and val will be the index pointing to the list
        # sort the distance list and count according to k
        res = []
        for (x, y) in points:
            dist = -(x ** 2 + y ** 2)
            if len(res) >= k:
                heapq.heappushpop(res, (dist, x, y))
            else:
                heapq.heappush(res, (dist, x, y))
        return [(x, y) for dist, x, y in res]  # O(klogn), O(n)


# Solution3: bucket sort