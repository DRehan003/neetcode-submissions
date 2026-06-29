class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        size = len(temperatures) - 1

        for i, x in enumerate(temperatures):
            if i == size:
                stack.append(0)
                break
            count = 1 
            while count != 0:
                if temperatures[i + count] > x:
                    stack.append(count)
                    break
                count += 1
                if i + count > size:
                    stack.append(0)
                    count = 0
            
        return stack