class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
    
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index1 >= index2:
                    continue
                if value1 + value2 == target:
                    solution.append(index1)
                    solution.append(index2)
                    return solution