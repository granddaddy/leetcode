class Solution:
    def combine(self, n: int, k: int):
        ret = []

        curr = [0]
        i = 0
        while True:
            if i == -1:
                break

            curr[i] += 1

            if curr[i] > n - (k - i - 1):
                curr.pop()
                i -= 1
                continue

            if i < k - 1:
                curr.append(curr[i])
                i += 1
                continue

            if i == k - 1:
                print(curr)
                ret.append(curr[:])

        return ret
s = Solution()
print(s.combine(6,4))
