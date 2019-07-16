import heapq

class Solution:
    def cutOffTree(self, forest):
        if not forest:
            return -1

        n = len(forest)
        m = len(forest[0])

        def find_path(src, dst):
            q = [(src, 0)]
            visited = {src: True}

            if src == dst:
                return 0

            while q:
                c, c_d = q.pop(0)
                c_i, c_j = c

                i = 0
                for j in [-1, 1]:
                    n_i, n_j = c_i + i, c_j + j
                    if max(n_j, 0) == n_j and min(n_j, m-1) == n_j and forest[n_i][n_j] and (n_i, n_j) not in visited:
                        if (n_i, n_j) == dst:
                            return c_d + 1
                        visited[(n_i, n_j)] = True
                        q.append(((n_i, n_j), c_d+1))
                j = 0
                for i in [-1, 1]:
                    n_i, n_j = c_i + i, c_j + j
                    if max(n_i, 0) == n_i and min(n_i, n-1) == n_i and forest[n_i][n_j] and (n_i, n_j) not in visited:
                        if (n_i, n_j) == dst:
                            return c_d + 1
                        visited[(n_i, n_j)] = True
                        q.append(((n_i, n_j), c_d+1))

            return None

        heap = []
        for i in range(n):
            for j in range(m):
                f = forest[i][j]
                if f > 1:
                    heapq.heappush(heap, (f, i, j))

        curr = (0, 0)
        curr_dst = 0

        # print(heap)
        # for l in forest:
        #     print(l)

        while heap:
            poss = []
            f, i, j = heapq.heappop(heap)
            _dst = find_path(curr, (i, j))
            # print(f, i, j, _dst)
            if _dst == None:
                return -1
            curr_dst += _dst
            curr = (i, j)

        # print(curr_dst)
        return curr_dst


s = Solution()

# o = s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]])
# assert(o == 6)
# o = s.cutOffTree([
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ])
# assert(o == -1)
# o = s.cutOffTree([
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ])
# assert(o == 6)

o = s.cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]])
assert(o == 57)
