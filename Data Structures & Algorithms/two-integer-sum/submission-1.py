class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        look={}
        for i in range (len(nums)):
            search = target - nums[i]
            if search in look:
                return [look[search], i]

            else:
                look[nums[i]] = i

        return False