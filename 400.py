class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 9
        digits = 1
        while n >= start * digits:
            n -= start * digits
            digits += 1
            start *= 10
        start = 10 ** (digits - 1)
        number = start + (n - 1) // digits
        return int(str(number)[n%digits -1])


New = Solution()
New.findNthDigit(190)