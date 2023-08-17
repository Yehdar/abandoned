class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in dict:
                return [index, dict[diff]]
            dict[value] = index
        return []
