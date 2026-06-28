class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # this removes duplicates
        sequence = 0
        streak = 0

        for x in nums:
            if x-1 in nums:
                continue 

            else:
                for y in range(len(nums)):
                    if x+y in nums:
                        sequence += 1
                    else:    
                        break

                if sequence > streak:
                    streak = sequence
                
                sequence = 0

        return streak