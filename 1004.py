from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        global_max = 0
        cnt = 0
        while right < len(A):
            if A[right] == 1:
                right += 1
                global_max = max(global_max, right - left)
            elif cnt < K:
                cnt += 1
                right += 1
                global_max = max(global_max, right - left)
            elif cnt == K:
                if A[left] == 0:
                    cnt -= 1
                left += 1
        return global_max


New = Solution()
New.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)