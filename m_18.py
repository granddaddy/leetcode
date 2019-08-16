class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        p = {}
        for i in range(n):
            for j in range(min(i+1, n),n):
                _i = nums[i]
                _j = nums[j]
                s = _i + _j
                if s not in p:
                    p[s] = {}
                p[s][(min(i,j), max(i,j))] = True

        print(p)
        ret = {}
        ks = list(p.keys())
        while True:
            if not ks:
                break
            k = ks.pop()
            if p[k] and target - k in p and p[target - k]:
                if target - k != k:
                    ks.pop(ks.index(target - k))
                x = list(p[k].keys())
                y = list(p[target - k].keys())

                while True:
                    if not x:
                        break
                    _x = x.pop()
                    for _y in y:
                        if _x[0] != _y[0] and _x[1] != _y[0] and _x[0] != _y[1] and _x[1] != _y[1]:
                            z = sorted([nums[_x[0]], nums[_x[1]], nums[_y[0]], nums[_y[1]]])
                            z = tuple(z)
                            ret[z] = True

        return list(map(lambda x: list(x), ret.keys()))

s = Solution()
o = s.fourSum([1, 0, -1, 0, -2, 2], 0)
e = [
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

print(o)
assert(len(e) == len(o))
for _e in e:
    assert(_e in o)
