from typing import List
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        hashtable={}
        i=0
        res=0
        while i <len(points):
            j=0
            hashtable.clear()
            while j <len(points):
                if j==i:
                    j+=1
                    continue
                dis=(points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                if dis in hashtable:
                    hashtable[dis]+=1
                else:
                    hashtable[dis]=1
                j+=1
            i+=1
            for k in hashtable:
                if hashtable[k]>1:
                    res+=hashtable[k]*(hashtable[k]-1)
        return res


New = Solution()
New.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])