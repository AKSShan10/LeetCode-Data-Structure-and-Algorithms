class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minH = []
        for x,y in points:
            dis = (x**2)+(y**2)
            minH.append([dis,x,y])
        heapq.heapify(minH)
        res = []
        while k>0:
            dis,x,y = heapq.heappop(minH)
            res.append([x,y])
            k-=1
        return res