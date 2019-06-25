import math

class Solution:
    dp = {}

    def superEggDropHelper(self, K: int, N: int) -> int:
        self.total_r += 1
        # print(K, N)

        if N == 0 or N == 1:
            return N

        else:
            half = math.ceil(N/2)
            if K > half:
                KK = half
            else:
                KK = K

            if (KK, N) in self.dp:
                return self.dp[(KK,N)]

            vv = N
            if K >= 2:
                r = range(1, half+1)
            else:
                r = [KK]

            for i in r:
                bottom_N = i - 1
                top_N = N - i

                v = 1 + max(
                    self.superEggDropHelper(KK - 1, bottom_N),
                    self.superEggDropHelper(KK, top_N)
                )

                if v < vv:
                    vv = v

            self.dp[(KK,N)] = vv
            print(self.dp)
            return vv

    def superEggDrop(self, K: int, N: int) -> int:
        self.total_r = 0
        v = self.superEggDropHelper(K, N)
        print("total: " + str(self.total_r))
        return v

s = Solution()
assert(s.superEggDrop(2,9) == 4)
# assert(s.superEggDrop(2,7) == 4)
# assert(s.superEggDrop(1,3) == 3)
# assert(s.superEggDrop(2,6) == 3)
# assert(s.superEggDrop(1,2) == 2)
# assert(s.superEggDrop(3,14) == 4)
# assert(s.superEggDrop(100,10000))
