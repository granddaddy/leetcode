class Solution:
    def maximalSquare(self, matrix):
        largest = 0

        if not matrix:
            return largest

        NN = len(matrix)
        MM = len(matrix[0])

        def in_b(i, j):
            if i < NN and j < MM:
                return True
            return False

        def f_l_s(i, j):
            n = 1
            while True:
                _n = n + 1
                if not in_b(i+n,j+n):
                    return n
                else:
                    # print(i, j, n, _n)
                    a = all([x == '1' for x in matrix[i+n][j:j+_n]])
                    b = all([x[j+n] == '1' for x in matrix[i:i+_n]])
                    if a and b:
                        n = _n
                    else:
                        return n


        for i in range(NN):
            for j in range(MM):
                if matrix[i][j] == '1':
                    k = f_l_s(i, j)
                    if k > largest:
                        largest = k

        # print(largest)
        return largest**2

s = Solution()
r = s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
assert(r == 4)
r = s.maximalSquare([["1","0"],["1","0"]])
assert(r == 1)
r = s.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])
