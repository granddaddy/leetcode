class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        ret = [[]]

        n = len(nums)

        i = 0
        ii = 0
        last = None
        last_m = 0

        while i < n:
            num = nums[i]
            m = len(ret)
            if num == last:
                ii = last_m
            else:
                ii = 0
            while True:
                r = ret[ii]
                if ii >= m:
                    break
                c = r[:]
                c.append(num)
                ret.append(c)
                ii += 1

            i += 1
            last = num
            last_m = m

        return ret

s = Solution()
print(s.subsetsWithDup([1,2,2]))

print("###")
print(s.subsetsWithDup([1,2,2,2,2,2,]))
