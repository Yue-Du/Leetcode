class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result=n
        while result>1:
            result = result/2
        if result ==1:
            return True
        else:
            return False


New = Solution()
New.isPowerOfTwo(3)