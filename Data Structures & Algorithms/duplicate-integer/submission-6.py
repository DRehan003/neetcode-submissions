class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for i in nums:
            if i in nums2:
                return True
            nums2.add(i)

        return False