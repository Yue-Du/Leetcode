class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        up=num
        low=0
        med=num
        if num ==1:
            return True
        while (up-low) >1:
            if med*med == num:
                return True
            elif med*med>num:
                up = med
                if (up-low)%2==0:
                    med=low+(up-low)/2
                else:
                    med=low+(up-low+1)/2
            else:
                low = med
                if (up-low)%2==0:
                    med=low+(up-low)/2
                else:
                    med=low+(up-low+1)/2
        return False


New = Solution()
New.isPerfectSquare(14)