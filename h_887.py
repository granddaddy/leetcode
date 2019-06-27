import math

class Solution:
    dp = {}

    def superEggDropHelper(self, K: int, N: int) -> int:
        self.total_r += 1
        # print(K, N)

        if K == 0:
            return 0

        if N == 0 or N == 1 or K == 1:
            return N

        if (K, N) in self.dp:
            return self.dp[(K,N)]

        low = 2
        high = N
        vv = N
        while True:
            mid = math.ceil((high+low) / 2)
            bottom_N = mid - 1
            top_N = N - mid

            top_sol = self.superEggDropHelper(K, top_N)
            bott_sol = self.superEggDropHelper(K - 1, bottom_N)

            v = 1 + max(top_sol, bott_sol)
            if v < vv:
                vv = v

            if high == low or top_sol == bott_sol:
                break

            if top_sol > bott_sol:
                low = mid
            else:
                if mid == high:
                    high = low
                else:
                    high = mid


        self.dp[(K,N)] = vv
        # print(self.dp)
        return vv

    def superEggDrop(self, K: int, N: int) -> int:
        self.total_r = 0
        v = self.superEggDropHelper(K, N)
        # print("total: " + str(self.total_r))
        return v

s = Solution()
assert(s.superEggDrop(2,9) == 4)
assert(s.superEggDrop(2,11) == 5)
assert(s.superEggDrop(3,11) == 4)
assert(s.superEggDrop(2,7) == 4)
assert(s.superEggDrop(1,3) == 3)
assert(s.superEggDrop(2,6) == 3)
assert(s.superEggDrop(1,2) == 2)
assert(s.superEggDrop(3,14) == 4)
assert(s.superEggDrop(100,10000))
