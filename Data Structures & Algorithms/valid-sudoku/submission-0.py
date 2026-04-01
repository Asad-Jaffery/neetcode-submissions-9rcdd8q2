class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows:
        for i in range(len(board)):
            nums = set()
            for j in range(len(board[i])):
                if board[i][j] in nums:
                    print("r")
                    return False
                elif board[i][j] != ".":
                    nums.add(board[i][j])

        # check cols
        for i in range(len(board)):
            nums = set()
            for j in range(len(board[i])):
                if board[j][i] in nums:
                    print("c")
                    return False
                elif board[j][i] != ".":
                    nums.add(board[j][i])

        # create another board
        square_board = [[set(), set(), set()],
                        [set(), set(), set()],
                        [set(), set(), set()]]
        
        # check squares
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in square_board[i // 3][j // 3]:
                    print("s")
                    return False
                elif board[i][j] != ".":
                    square_board[i // 3][j // 3].add(board[i][j])
        return True







        