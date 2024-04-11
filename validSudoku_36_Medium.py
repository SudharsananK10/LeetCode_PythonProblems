class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      
        for c in range(0,9):
            # Row check
            if len([k for k,v in Counter(board[c]).items() if k!='.' and v>1]) > 0:
                return False
            vl=[]
            for r in range(0,9):
                vl.append(board[r][c])
            # Column Check
            if len([k for k,v in Counter(vl).items() if k!='.' and v>1]) > 0:
                return False

        for i in [3,6,9]:
            for j in [3,6,9]:
                sql=[]
                for r in range(i-3,i):
                    for c in range(j-3,j):
                        print("r={}; c={}".format(r,c))
                        sql.append(board[r][c])
                #Box Check
                if len([k for k,v in Counter(sql).items() if k!='.' and v>1]) > 0:
                    return False

        return True

