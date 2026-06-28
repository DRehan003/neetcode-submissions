class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqS, freqT = {}, {}

        for char in s:
            if char not in freqS:
                freqS[char] = 1
            else:
                freqS[char] += 1

        for char in t:
            if char not in freqT:
                freqT[char] = 1
            else:
                freqT[char] += 1

        for key, value in freqS.items():
            if key in freqT and freqT[key] == value:
                continue
            else:
                return False

        return True