from functools import reduce
class Solution:
    def isHappy(self, n: int) -> bool:
        cach = []
        while n != 1:
            if n not in cach:
                cach.append(n)
                num = list(str(n))
                if len(num) > 1:
                    n=sum(map(lambda x: pow(int(x),2), num))
                else:
                    n = pow(int(num[0]), 2)
            else:
                return False
        return True


New = Solution()
New.isHappy(78)