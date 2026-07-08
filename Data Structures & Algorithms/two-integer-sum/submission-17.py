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
            # if j in hashmap then return [hashmap[j], i]
            if target - value in hashmap:
                return [hashmap[target - value], i]
            hashmap[value] = i