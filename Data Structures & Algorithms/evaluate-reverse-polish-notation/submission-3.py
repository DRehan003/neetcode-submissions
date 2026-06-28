class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda z : z[-2] + z[-1],
            "-": lambda z : z[-2] - z[-1], 
            "*": lambda z : z[-2] * z[-1], 
            "/": lambda z : int(z[-2] / z[-1])
            }

        for x in tokens:
            if x not in operators: 
                stack.append(int(x))
            else:
                if stack:
                    stack[-1] = operators[x](stack)
                    stack.pop(-2)
    
        return stack[-1]     