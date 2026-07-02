class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean string
        palindrome = []

        for char in s:
            if char.isalnum():
                palindrome.append(char.lower())
        
        # 2 pointer iteration
        L = 0
        R = len(palindrome) - 1

        while L < R:
            if palindrome[L] == palindrome[R]:
                L += 1
                R -= 1
            else:
                return False

        return True