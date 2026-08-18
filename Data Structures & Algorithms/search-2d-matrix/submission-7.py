class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        total = m*n
        l,r = 0, total-1
        while l<=r:
            print("l=", l, " r=", r)
            mp = (l+r)//2
            print("mp=",mp)
            row = mp//n
            col = mp%n
            print("row=",row, "col=",col)
            num = matrix[row][col]
            print("num=",num)
            if num == target:
                return True

            elif num > target:
                r=mp-1
            
            else:
                l=mp+1

        return False