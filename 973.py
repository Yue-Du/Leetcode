from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        i = 0
        while i < len(points):
            dis = pow(points[i][0],2)+pow(points[i][1],2)
            if i < K:
                heapq.heappush(heap,[-1 * dis, points[i]])
            else:
                if -1*dis > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,[-1* dis, points[i]])
            i+=1
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res


New = Solution()
New.kClosest([[1,3],[-2,2]], 1)
