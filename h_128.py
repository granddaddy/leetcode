class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        d = {}
        for n in nums:
            if n - 1 in d:
                d[n-1] = n
            if n + 1 in d:
                d[n] = n + 1
            else:
                d[n] = n

        longest = 1
        print(d)
        while d:
            x0 = next(iter(d))
            leng = 1

            y0 = x0 - 1
            while True:
                v = d.pop(y0, None)
                if v == None:
                    break
                leng += 1
                y0 -= 1

            while True:
                x1 = d.pop(x0, None)
                if x1 == None:
                    break
                if x1 == x0:
                    break
                leng += 1
                x0 = x1

            longest = max(longest, leng)

        return longest
