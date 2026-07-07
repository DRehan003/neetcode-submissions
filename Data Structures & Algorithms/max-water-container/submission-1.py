class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # compute and return max area
        # You may choose any two bars to form a container.

        # 1. height is capped by the shorter leg
        # 2. value and index
        # 3. none
        # 4. 2 pointer
        # 5. check what the min leg is 


        # create pointers and maximum var
        l, r = 0, len(heights) - 1
        maximum = 0

        # while right > left
        while r > l:
            area = (r - l) * min(heights[r], heights[l])
            # if area > maximum then set maximum to area
            if area > maximum:
                maximum = area
            # if nums[r] > nums[l] then increment left by 1
            if heights[r] > heights[l]:
                l += 1
            # else decrease right by 1
            else:
                r -= 1

        return maximum
