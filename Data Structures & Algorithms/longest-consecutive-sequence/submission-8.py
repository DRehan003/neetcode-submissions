class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # this removes duplicates
        longest = 0

        for x in nums:
            if x-1 not in nums:
                length = 0

                while x + length in nums:
                    length += 1

                longest = max(longest, length)

        return longest