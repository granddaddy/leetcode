class Solution:
    def countRangeSum(self, nums, lower, upper) -> int:
        def in_range(x):
            return upper >= x and x >= lower

        if not nums:
            return 0

        N = len(nums)

        # make start prettier
        w = {0: 0}
        ret = 0

        for i, num in enumerate(nums, 1):
            m = min(i, N)
            for j in range(m, 0, -1):
                if i == m:
                    _w = w[j-1]
                    new = _w + num
                else:
                    _w = w[j]
                    _diff = nums[i-m-1]
                    new = _w + num - diff

                w[j] = new
                if in_range(new):
                    ret += 1

            #     print(w)
            # print()

        # print(ret)
        return ret
