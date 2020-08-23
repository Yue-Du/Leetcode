from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        output = []
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                two_sum = nums[i] + nums[j]
                k = j + 1
                while k < len(nums):
                    if two_sum + nums[k] == 0:
                        output.append([nums[i], nums[j], nums[k]])
                        break
                    else:
                        k = k + 1
                j = j + 1
            i = i + 1
        g = 0
        while g < len(output):
            output[g] = sorted(output[g])
            g = g + 1
        h = 0
        new_output = []
        while h < len(output):
            if output[h] not in new_output:
                new_output.append(output[h])
            h = h + 1

        return output


New = Solution()
New.threeSum([-1,0,1,2,-1,-4])