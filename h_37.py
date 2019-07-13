def getSubBox(i, j):
    sub_b_i = int(i/3)
    sub_b_j = int(j/3)

    return sub_b_i, sub_b_j

def to_bit(i):
    return (1 << int(i) - 1)

def to_int(p):
    i = 0
    while p > 0:
        if p == 1:
            return i + 1
        p = p >> 1
        i += 1

def inv_to_int(p):
    i = 0
    while p > 0:
        if p & 1 == 0:
            return i + 1
        p = p >> 1
        i += 1

class Solution:

    def firstPass(self):
        i = 0
        j = 0

        while i < 9:
            yield (i, j)

            j += 1
            if j == 9:
                i += 1
                j = 0

    def subBoxRange(self, sub_b_i, sub_b_j):
        _i = 0
        _j = 0

        while _i < 3:
            ret_i = sub_b_i + _i
            ret_j = sub_b_j + _i
            yield(ret_i, ret_j)

            _j += 1
            if _j == 3:
                _i += 1
                _j = 0

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        print(board)
        d_s = {}

        r_ix = {}
        c_ix = {}
        sb_ix = {}

        def addIdx(i, j):
            if i in r_ix:
                r_ix[i][j] = True
            else:
                r_ix[i] = {j: True}

            if j in c_ix:
                c_ix[j][i] = True
            else:
                c_ix[j] = {i: True}

            x, y = getSubBox(i, j)
            if (x, y) in sb_ix:
                sb_ix[(x,y)][(i,j)] = True
            else:
                sb_ix[(x,y)]  = {(i,j): True}

        def findPoss(i, j):
            # row
            r = 0
            for x in board[i]:
                if x != '.':
                    r |= to_bit(int(x))

            c = 0
            for _i in range(9):
                x = board[_i][j]
                if x != '.':
                    c |= to_bit(int(x))

            s = 0
            sub_b_i, sub_b_j = getSubBox(i, j)
            for _i, _j in self.subBoxRange(sub_b_i, sub_b_j):
                x = board[_i][_j]
                if x != '.':
                    s |= to_bit(int(x))

            p = r | c | s

            _count = bin(p).count("1")
            if _count == 8:
                _p = inv_to_int(p)
                board[i][j] = str(_p)
            else:
                d_s[(i,j)] = p
                addIdx(i, j)

        for i, j in self.firstPass():
            if board[i][j] == '.':
                findPoss(i, j)

        print(board)
        print(d_s)

s = Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

assert(getSubBox(0, 0) == (0, 0))
assert(getSubBox(3, 0) == (1, 0))
assert(getSubBox(3, 3) == (1, 1))
assert(getSubBox(6, 3) == (2, 1))

assert(to_int(to_bit(1)) == 1)
assert(to_int(to_bit(2)) == 2)
assert(to_int(to_bit(9)) == 9)

p = 0
for i in range(1,10):
    if i != 7:
        p |= to_bit(int(i))

assert(inv_to_int(p) == 7)
