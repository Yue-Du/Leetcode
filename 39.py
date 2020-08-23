from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)

        def helper(target, res, cur, index):
            if target == 0:
                return res.append(cur[:])
            elif index == len(nums) or nums[index] > target:
                return res

            helper(target - nums[index], res, cur + [nums[index]],index)
            helper(target, res, cur, index + 1)
            return res

        return helper(target, [], [], 0)


New = Solution()
New.combinationSum([8,7,4,3],11)