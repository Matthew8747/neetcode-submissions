class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}


        for char in t:
            if char in dictT:
                dictT[char] = (dictT[char] + 1)
            else:
                dictT[char] = 1

        for char in s:
            if char in dictS:
                dictS[char] = (dictS[char] + 1)
            else:
                dictS[char] = 1

        if dictT == dictS:
            return True
        return False       