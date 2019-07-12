class Solution:

    def helper(self, a, b, s):
        if not s:
            return True

        t = a+b
        s_t = str(t)
        if s.startswith(s_t):
            return self.helper(b, t, s[len(s_t):])
        return False


    def isAdditiveNumber(self, num):
        i, j, n = 1, 1, len(num)
        while True:
            r = n - i - j
            if r < i and j == 1:
                return False
            if r < j:
                i += 1
                j = 1
                continue

            s_i = num[:i]
            s_j = num[i:i+j]

            if i > 1 and s_i[0] == "0":
                return False
            if j > 1 and s_j[0] == "0":
                i += 1
                j = 1
                continue

            n_i, n_j = int(s_i), int(s_j)
            print(n_i, n_j)

            su = n_i + n_j
            s_su = str(su)
            n_su = len(s_su)

            if r < n_su:
                i += 1
                j = 1
                continue

            if self.helper(n_i, n_j, num[i+j:]):
                return True

            j += 1

s = Solution()
assert(s.isAdditiveNumber("1203") == False)
assert(s.isAdditiveNumber("1023") == False)
assert(s.isAdditiveNumber("111") == False)
assert(s.isAdditiveNumber("199111992") == True)
assert(s.isAdditiveNumber("0235813") == False)
assert(s.isAdditiveNumber("112358") == True)
assert(s.isAdditiveNumber("199100199") == True)
