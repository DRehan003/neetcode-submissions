class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            pass
        else:
            return False

        dictS = {}
        dictT = {}
        
        for char in s:
            if char in dictS:
                dictS[char] += 1
            else:
                dictS[char] = 1

        for char in t:
            if char in dictT:
                dictT[char] += 1
            else:
                dictT[char] = 1

        for value in dictS:
            if value in dictT and dictS[value] == dictT[value]:
                pass
            else:
                return False
        
        return True
