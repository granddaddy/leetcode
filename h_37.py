import heapq

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
    for i in range(9):
        if p & 1 == 0:
            break
        p = p >> 1
    return i + 1

def subBoxRange(sub_b_i, sub_b_j):
    _i = 0
    _j = 0

    while _i < 3:
        ret_i = sub_b_i * 3 + _i
        ret_j = sub_b_j * 3 + _j
        yield(ret_i, ret_j)

        _j += 1
        if _j == 3:
            _i += 1
            _j = 0

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

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for _r in board:
            print(_r)
        d_s = {}

        r_ix = {}
        c_ix = {}
        sb_ix = {}

        def addIdx(i, j, p):
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
                sb_ix[(x,y)] = {(i,j): True}

        def update(i, j, p):
            if (i, j) not in d_s:
                return
            print(i, j, p)
            old = d_s[(i,j)]

            if p:
                new = old | to_bit(p)
                d_s[(i,j)] = new
            else:
                new = old

            _count = bin(new).count("1")
            if _count == 8:
                _new = inv_to_int(new)
                board[i][j] = str(_new)
                print("setting", i, j, new, _new)

                x, y = getSubBox(i, j)

                r_ix[i].pop(j)
                c_ix[j].pop(i)
                sb_ix[(x,y)].pop((i,j))
                d_s.pop((i,j))

                rr = list(r_ix[i].keys())
                for _j in rr:
                    update(i, _j, _new)
                cc = list(c_ix[j].keys())
                for _i in cc:
                    update(_i, j, _new)
                ss = list(sb_ix[(x,y)].keys())
                for _i, _j in ss:
                    update(_i, _j, _new)

        def visit(i, j):
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
            for _i, _j in subBoxRange(sub_b_i, sub_b_j):
                x = board[_i][_j]
                if x != '.':
                    s |= to_bit(int(x))

            p = r | c | s

            addIdx(i, j, p)
            d_s[(i,j)] = p

        for i, j in self.firstPass():
            if board[i][j] == '.':
                visit(i, j)

        print(d_s)

        dd = list(d_s.keys())
        for i, j in dd:
            update(i, j, 0)

        h = []
        while True:
            dd = list(d_s.keys())
            if not dd:
                return

            for k in dd:
                v = d_s[k]
                _count = bin(v).count("0") - 1
                heapq.heappush(h, (_count, k, v))

            print(h)
            break
            # for i, j in dd:
            #     update(i, j, 0)

        for _r in board:
            print(_r)
        print(d_s)

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
p = 0
for i in range(1,10):
    if i != 9:
        p |= to_bit(int(i))
assert(inv_to_int(p) == 9)

sub_b_i, sub_b_j = getSubBox(6, 4)
# print(list(subBoxRange(sub_b_i, sub_b_j)))

s = Solution()
# s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

i = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
e = [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
s.solveSudoku(i)
for _r in e:
    print(_r)
assert(i == e)
