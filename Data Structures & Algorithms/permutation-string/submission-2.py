class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0,0
        s1Count={}
        length1 = len(s1)
        length2 = len(s2)
        if length2<length1: # just speed up a bit
            return False


        for char in s1:
            s1Count[char] = s1Count.get(char, 0) +1
        #creates the frequency hash table

        s2Count={}
        while r < length1:
            s2Count[s2[r]] = s2Count.get(s2[r], 0) +1
            r += 1
   


        while r < length2:
            if s2Count == s1Count:
                return True
            s2Count[s2[r]] = s2Count.get(s2[r], 0) +1
            
            r += 1
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == 0:
                del s2Count[s2[l]]
            l += 1

        if s2Count == s1Count:
            return True
            
        return False            



        