class C:
    def __init__(self, _a0, _a1):
        self.a = (_a0, _a1)

    def __sub__(self, o):
        return (self.a[0] - o.a[0]) + (self.a[1] - o.a[1])

    def __getitem__(self, index):
        return self.a[index]

    def __str__(self):
        return "("+str(self.a[0])+","+str(self.a[1])+")"

class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        for m in matrix:
            print(m)

        def get(tup):
            return matrix[tup[0]][tup[1]]

        def half(mn, mx):
            if mn == mx:
                return mn
            if mn[0] == mx[0]:
                new_0 = mn[0]
                new_1 = (mn[1] + mx[1]) // 2
            else:
                new_0 = (mn[0] + mx[0]) // 2
                new_1 = mn[1]
            return C(new_0, new_1)

        def _find(mn, mx, ge):
            while True:
                if mx - mn == 0:
                    return mn

                if target <= get(mn):
                    return mn

                if get(mx) <= target:
                    return mx

                if mx - mn == 1:
                    if ge:
                        return mx
                    return mn

                h = half(mn, mx)
                hv = get(h)

                if hv == target:
                    return h

                if hv < target:
                    mn = h
                else:
                    mx = h

        def find_le(mn, mx):
            return _find(mn, mx, ge=False)

        def find_ge(mn, mx):
            return _find(mn, mx, ge=True)

        N = len(matrix)
        old_min_n = 0
        old_max_n = N - 1

        M = len(matrix[0])
        old_min_m = 0
        old_max_m = M - 1

        while True:
            _mn = find_le(C(old_min_n, old_max_m), C(old_max_n, old_max_m))
            _mx = find_ge(C(old_min_n, old_min_m), C(old_max_n, old_min_m))

            if get(_mn) == target or get(_mx) == target:
                return True

            new_min_n, _ = _mn
            new_max_n, _ = _mx

            if get(_mn) <= target:
                new_min_n = min(new_min_n + 1, old_max_n)
            if get(_mx) >= target:
                new_max_n = max(new_max_n - 1, old_min_n)

            _mn = find_le(C(old_max_n, old_min_m), C(old_max_n, old_max_m))
            _mx = find_ge(C(old_min_n, old_min_m), C(old_min_n, old_max_m))

            if get(_mn) == target or get(_mx) == target:
                return True

            _, new_min_m = _mn
            _, new_max_m = _mx

            if get(_mn) <= target:
                new_min_m = min(new_min_m + 1, new_max_m)
            if get(_mx) >= target:
                new_max_m = max(new_max_m - 1, new_min_m)

            old = (old_min_n, old_max_n, old_min_m, old_max_m)
            new = (new_min_n, new_max_n, new_min_m, new_max_m)

            print(new)
            if old == new:
                break
            else:
                old_min_n, old_max_n, old_min_m, old_max_m = new

        return False

s = Solution()
# m = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# assert(s.searchMatrix(m, 15))
# assert(s.searchMatrix(m, 16))
# assert(s.searchMatrix(m, 20) == False)
#
# m = [[-5]]
# assert(s.searchMatrix(m, -2) == False)
#
# m = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# 5
# assert(s.searchMatrix(m, 5))

m = [[4,7,12,17],[4,9,17,21],[4,12,17,21]]
assert(s.searchMatrix(m, 5) == False)
