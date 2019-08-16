class Solution:
    def findCircleNum(self, M):
        for _m in M:
            print(_m)
        print("####")
        N = len(M)

        if not N:
            return 0

        f_circle = list(range(N))

        def set_f_circle(mn, i):
            if f_circle[mn] == mn:
                old = f_circle[i]
                for j in range(N):
                    if f_circle[j] == old:
                        f_circle[j] = mn

            else:
                set_f_circle(f_circle[mn], i)

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if M[i][j] == 1:
                    mn = min(f_circle[i], f_circle[j])
                    set_f_circle(mn, i)
                    set_f_circle(mn, j)
                    print(mn, i, j)
                    print(f_circle)

        print(f_circle)
        return sum(map(lambda i: 1 if f_circle[i] == i else 0, range(N)))

s = Solution()
M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(s.findCircleNum(M))
