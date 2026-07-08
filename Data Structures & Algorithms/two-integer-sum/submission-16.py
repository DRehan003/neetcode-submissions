class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Only one valid answer exists
        # 2. value and index
        # 3. none
        # 4. hashmap
        # 5. if j in hashmap

        # create hashmap
        hashmap = {}

        # enumerate through nums, values are the index and key are index
        for i, value in enumerate(nums):
            # if j in hashmap then return sort([i, nums[j] ])
            j = target - value
            if j in hashmap:
                return [hashmap[j], i]
            hashmap[value] = i