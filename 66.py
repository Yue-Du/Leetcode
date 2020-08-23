from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        if len(set(digits))==1 and digits[0]==9:
            for i in range(length):
                digits[i]=0
            digits.insert(0,1)
            return digits
        i=length-1
        while i >=0 :
            if digits[i]==9:
                i=i-1
            else:
                digits[i]=digits[i]+1
                j=i+1
                while j<length:
                    digits[j]=0
                    j=j+1
                return digits


new = Solution()
new.plusOne([1,2,9,9])