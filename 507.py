import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        sum = 0
        i = math.floor(math.sqrt(num))
        while i > 0:
            if num % i == 0:
                shang = num // i
                if shang == i:
                    sum += i
                elif i == 1:
                    sum += i
                else:
                    sum += i
                    sum += shang
                if sum > num:
                    return False
            i -= 1
        if sum == num:
            return True
        else:
            return False


New = Solution()
New.checkPerfectNumber(28)