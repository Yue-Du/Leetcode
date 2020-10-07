class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            k=0
            for j in str(i):
                k+=int(j)#转为字符串后得位数和
            if k in d:
                d[k]+=1
            else:
                d[k]=1
        max_val = 0
        max_cnt = 0
        for key in d:
            if d[key]> max_val:
                max_val = d[key]
                max_cnt = 1
            elif d[key] == max_val:
                max_cnt += 1

        return max_cnt

New = Solution()
New.countLargestGroup(13)