import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = re.sub(r'[\W_]', '', s)

        pL=0
        pR=len(s)-1
        while pL < pR:
            if s[pL] != s[pR]:
                return False
            print(s[pL])
            print(s[pR])
            pL +=1
            pR -=1

        return True