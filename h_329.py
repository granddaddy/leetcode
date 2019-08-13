from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        N = len(matrix)
        M = len(matrix[0])

        def in_matrix(i, j):
            if 0 <= i and i < N:
                if 0 <= j and j < M:
                    return True
            return False

        def get(i, j):
            return matrix[i][j]

        def find_adjs(i, j, n0):
            dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            adjs = []
            for d in dirs:
                if in_matrix(*d) and get(*d) < n0:
                    adjs.append(d)

            return adjs


        edges = {}
        p_st = []
        for i in range(N):
            for j in range(M):
                n0 = get(i, j)
                adjs = find_adjs(i, j, n0)

                if not adjs:
                    p_st.append((i, j))

                for a in adjs:
                    _a = edges.setdefault(a, [])
                    _a.append((i, j))

        @lru_cache(None)
        def l_path(i, j):
            if (i, j) not in edges:
                return 1

            _mx = 1
            for _ij in edges[(i, j)]:
                _mx = max(_mx, 1 + l_path(*_ij))
            return _mx

        _mx = 0
        for ps in p_st:
            _mx = max(_mx, l_path(*ps))

        return _mx
