class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            if n and 1:
                cnt += 1
            n = n >> 1
        return cnt


New = Solution()
New.hammingWeight(00000000000000000000000000001011)