class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort in descending order. [[position], [speed]]
        pairs = sorted(zip(position, speed), key = lambda x: x[0], reverse = True) 

        #empty stack
        stack = []

        #loop through cars
        for x in pairs:
            #time to target
            distance = target - x[0]
            time = distance / x[1]

            # if current time <= top of stack, this car joins that fleet, pop current
            if not stack or time > stack[-1]:
                stack.append(time)
                
            #push time to stack

        #return size of stack
        return len(stack)