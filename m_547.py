_print = print

def print(msg):
    if True:
        _print(msg)

class Solution:
    def findCircleNum(self, M):
        # for _m in M:
        #     print(_m)
        # print("####")
        N = len(M)

        if not N:
            return 0

        f_circle = list(range(N))

        def find(i):
            if f_circle[i] == i:
                return i
            else:
                return find(f_circle[i])

        def union(i, j):
            f_circle[find(i)] = find(j)

        for i in range(N):
            for j in range(N):
                if i != j and M[i][j] == 1:
                    union(i, j)

        # print(f_circle)
        return sum(map(lambda i: 1 if f_circle[i] == i else 0, range(N)))

s = Solution()
M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(s.findCircleNum(M))

M = [[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
print(s.findCircleNum(M))
