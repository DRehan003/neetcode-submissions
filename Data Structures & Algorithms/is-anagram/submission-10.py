class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sfreq, tfreq = {}, {}
        
        for char in s: 
            sfreq[char] = sfreq.get(char, 0) + 1

        for char in t:
            tfreq[char] = tfreq.get(char, 0) + 1

        for key in sfreq.keys():
            if key not in tfreq.keys() or sfreq[key] != tfreq[key]:
                return False

        return True

        