class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #rule 1
        #board[r] is already a list of 9 rows
        for r in range(9):
            if self.has_duplicate(board[r]):
                return False
        
        #rule 2
        for c in range(9):

            #create column array
            column = []
            for r in range(9):
                column.append(board[r][c])
            if self.has_duplicate(column):
                return False
        
        #rule 3
        #3 boxes across, 3 down, 9 total
        for box_r in range(3):
            for box_c in range(3):
                box = []

                for r in range(box_r * 3, box_r * 3 + 3):
                    for c in range(box_c * 3, box_c * 3 + 3):
                        box.append(board[r][c])

                if self.has_duplicate(box):
                    return False

        return True



    def has_duplicate(self, group: List[str]) -> bool:
        # create an identical list. but drop the empty cells with dots
        filled = []
        for v in group:
            if v != ".":
                filled.append(v)




        #basically bool if duplicate. If set is smaller, theres a duplicate
        return len(filled) != len(set(filled))