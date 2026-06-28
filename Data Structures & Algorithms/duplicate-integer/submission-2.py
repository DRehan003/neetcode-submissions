class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}

        for x in nums:
            if x not in dictionary:
                dictionary[x] = 1
            else:
                return True

        return False