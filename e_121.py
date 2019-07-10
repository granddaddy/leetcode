class Solution:
    def maxProfit(self, prices):
        local_max = 0

        n = len(prices)

        i = 0
        p0 = prices[i]
        for j in range(i+1, n):
            p1 = prices[j]
            if p1 < p0:
                p0 = p1
                continue
            d = p1 - p0
            if d > local_max:
                local_max = d

        return local_max

s = Solution()
i = [7,1,5,3,6,4]
e = 5
o = s.maxProfit(i)
assert(o == e)

i = [7,6,4,3,1]
e = 0
o = s.maxProfit(i)
assert(o == e)

i = [2,1,4]
e = 3
o = s.maxProfit(i)
assert(o == e)
