class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) # this removes duplicates
        sequence = []
        streak = 0

        for x in nums:
            if x-1 in nums:
                continue 

            else:
                for y in range(len(nums)):
                    if x+y in nums:
                        sequence.append(x+y)
                    else:    
                        break

                if len(sequence) > streak:
                    streak = len(sequence)
                
                sequence.clear()

        return streak