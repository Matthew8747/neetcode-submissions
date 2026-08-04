class Solution:

    def encode(self, strs: List[str]) -> str:
        mas  = ""
        for string in strs:
            currLen = len(string)
            mas = mas + str(currLen) + "#" + string
        print(mas)
        return mas

    def decode(self, s: str) -> List[str]:
        i=0
        strs=[]
        while i < len(s):
            val=""
            while s[i].isdigit() :
                val = val + str(s[i])
                i+=1
                print(val)
                print("TEST")



            print(val)
            i += 1          # move past '#'
            newStr = s[i:i + int(val)]
            strs.append(newStr)
            i += int(val)
            print(newStr)
        return strs
