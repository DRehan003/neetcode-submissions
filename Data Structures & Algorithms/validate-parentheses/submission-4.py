class Solution:
    def isValid(self, s: str) -> bool:
        openB = []
        pairs = {"(" : ")", "[" : "]", "{" : "}"}
        
        if len(s) % 2 != 0: 
            return False

        for x in s:
            if x in pairs.values():
                if openB and pairs[openB[-1]] == x:
                    openB.pop()
                else:
                    return False
            else:
                openB.append(x)

        return True if not openB else False