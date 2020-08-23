class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        while high >= low+1:
            mid=low+(high-low)//2
            if mid * mid >x:
                high = mid
            else:
                low = mid
        return mid


new = Solution()
new.mySqrt(8)