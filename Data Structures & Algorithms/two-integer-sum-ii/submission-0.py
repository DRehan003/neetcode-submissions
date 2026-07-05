class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order, increasing order
        # 1-indexed: means that we start index at 1 instead of 0
        # index1 < index2, index1 != index2
        # index1 + index2 = target
        # exactly one valid solution.
        # solution must be O(1) additional space.

        # create two pointer L and R, create the while loop
        L = 0
        R = len(numbers) - 1

        while L < R:
            # if L + R == target:
            if numbers[L] + numbers[R] == target:
                return [L+1, R+1]
                # return [index1 + 1, index2 + 1]

            #else if L + R > target:
            elif numbers[L] + numbers[R] > target:
                R -= 1
                # R -= 1

            # else if L + R < target:
            elif numbers[L] + numbers[R] < target:
                L += 1
                # L += 1

        # loop through the vales and return [index1 + 1, index2 + 1] 
        