class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #its pre sorted so u can just do a binary search
        #basically a binary search on what row then what col

        ROWS = len(matrix)
        COLS = len(matrix[0])


        #these are for row indices
        top = 0
        bot = ROWS -1

        #binary search the rows
        while top<=bot:
            row = (top+ bot) // 2 #floor div
            if target > matrix[row][-1]:
                #matrix[row][-1] is the last and largest value in this row. . We know target is past it so every row from here up is too small. Discard this row and everything above it .  Moving top to [row] + 1

                top = row+1
            elif target<matrix[row][0]:
                #matrix[row][0] is the first and smallest of the rows.  target comes before it so every row from here down is too big. moving the bottom search area to  [row] -1
                bot=row-1
            else:
                #neither check is fire which means this is the only row that could contain the target. its within the first and last col of the row
                break;

        #if the row search loop ended because pointers crossed rather than because of the break. No rows contained the target.
        #this happens when it falls into a gap between two rows.
        #Example.  8 . when one row ends at and and next starts at 10.  So not in matrix at all
        if not(top<= bot):
            return False


        #recomputes the row index we lost from the break        
        row=(top+bot)//2

        #l and r . are column indicies . checking possible left bound and right bound within the row/  
        l=0
        r=COLS-1
        while l<=r:
            m=(l+r)//2

            if target>matrix[row][m]:
                #target is bigger than the middle value so it can only be to the right. move left pointer up
                l=m+1
            elif target <matrix[row][m]:
                #target is smaller. so only to left. move right pointer down
                r=m-1

            else:
                #matrix[row][m] IS the target
                return True



        #Scenario where points crossed the Row range . but nevera actually matched.  (e.g. 13 in [10,11,16,20]).
        return False