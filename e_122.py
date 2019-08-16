class Solution:
    def maxProfit(self, prices):

s = Solution()
i = [7,1,5,3,6,4]
e = 7
o = s.maxProfit(i)
assert(o == e)

i = [1,2,3,4,5]
e = 4
o = s.maxProfit(i)
assert(o == e)

i = [7,6,4,3,1]
o = 0
o = s.maxProfit(i)
assert(o == e)
