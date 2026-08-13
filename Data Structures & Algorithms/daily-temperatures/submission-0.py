class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add number to stack
        # if number in stack at the end, value = 0
        res = [0] * len(temperatures)
        stack = []   #pair [temp, ind]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                sT, sI = stack.pop()
                res[sI] = i - sI

            stack.append([t, i])
        return res


        