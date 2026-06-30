class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            if target-v in hashmap:
                return sorted([i, hashmap[target-v]])
            hashmap[v] = i