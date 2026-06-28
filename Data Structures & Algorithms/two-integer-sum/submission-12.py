class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {index:value for index, value in enumerate(nums)}
        
        for x in numsDict:
            number = target - numsDict[x]
            if number in numsDict.values():
                for i in numsDict:
                    if numsDict[i] == number and i != x:
                        solution = [x, i]
                        return solution