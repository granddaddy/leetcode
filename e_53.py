class Solution:
    def maxSubArray(self, nums) -> int:
        s_i = 0
        while True:
            if nums[s_i] > 0:
                break
            s_i += 1

        n_total = 0
        p_total = nums[s_i]

        s = s_i
        e = s_i

        largest = p_total

        for i in range(s_i, len(nums)):
            c = nums[i]
            if c <= 0:
                n_total += c
            else:
                if c > (-1 * n_total):
                    e = i
                    p_total += c
                    if p_total > largest:
                        largest = p_total
                else:
                    if (-1 * n_total) >= p_total:
                        s = i
                        e = i
                        p_total = c
                        n_total = 0
                        if c > largest:
                            largest = c

        print(largest)
        return largest


s = Solution()

r = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
assert(r == 6)
r = s.maxSubArray([10,-7,1-7,1,30])
assert(r == 32)
