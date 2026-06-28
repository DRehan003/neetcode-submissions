class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        sol = []

        product = 1
        for x in nums:
            product *= x
            prefix.append(product)

        product = 1
        for x in reversed(nums):
            product *= x
            suffix.append(product)
        suffix.reverse()

        for x in range(len(nums)):
            left = prefix[x-1] if x - 1 > -1 else 1
            right = suffix[x+1] if x + 1 < len(nums) else 1
            sol.append(left*right)

        return sol