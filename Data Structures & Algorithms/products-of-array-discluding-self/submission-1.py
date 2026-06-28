class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq = {}
        sol = []

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        if 0 in freq and freq[0] > 1:
            for x in range(len(nums)):
                sol.append(0)
            return sol
        elif 0 in freq and freq[0] == 1:
            product = nums[0]
            
            for x in range(1, len(nums)):
                if nums[x] == 0:
                    continue
                product *= nums[x]
                
            for x in nums:
                if x != 0:
                    sol.append(0)
                else:
                    sol.append(product)
            return sol
        else:
            product = nums[0]
            
            for x in range(1, len(nums)):
                product *= nums[x]
            
            for x in nums:
                sol.append(int(product/x))

            return sol

            
