from functools import lru_cache

@lru_cache(None)
def p(*args):
    l = list(filter(lambda x: x != 0, args))
    return tuple(sorted(l))

@lru_cache(None)
def q(*args):
    l = list(filter(lambda x: x != None, args))
    return tuple(sorted(l))

class Solution:
    def combinationSum2(self, candidates, target):
        @lru_cache(None)
        def f(t):
            good = {}
            d = {0: [None]}
            need_rec = []
            need_rec_i = []
            for i, c in enumerate(candidates):
                if c > t:
                    continue
                if t-c in d:
                    for j in d[t-c]:
                        if p(t-c, c) in good:
                            good[p(t-c, c)][q(j,i)] = True
                        else:
                            good[p(t-c, c)] = {q(j,i): True}
                if c in d:
                    d[c].append(i)
                else:
                    d[c] = [i]

                if c < t:
                    need_rec.append(c)
                    need_rec_i.append(i)

            for j in range(len(need_rec)):
                c = need_rec[j]
                i = need_rec_i[j]
                r, r_i = f(t-c)
                for k in range(len(r)):
                    _r = r[k]
                    _r_i = r_i[k]
                    tup = p(c, *_r)
                    if tup not in good:
                        if i not in _r_i:
                            good[tup] = {q(i, *_r_i): True}

            ret = []
            ret_i = []
            # print(good)
            for k in good:
                for kk in good[k].keys():
                    ret.append(k)
                    ret_i.append(kk)

            # print(t)
            # print(ret)
            # print(ret_i)
            return ret, ret_i

        r, r_i = f(target)
        return list(map(lambda x: list(x), set(r)))

s = Solution()
input = [10,1,2,7,6,1,5]
target = 8
exp = [
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

def match(x, y):
    if len(x) != len(y):
        return False
    for xx in x:
        if xx not in y:
            return False

    for yy in y:
        if yy not in x:
            return False

    return True

o = s.combinationSum2(input, target)
assert(len(o) == len(exp))
for x in exp:
    a = False
    for y in o:
        if match(x, y):
            a = True
    assert(a)

input  = [2,5,2,1,2]
target = 5
exp = [
  [1,2,2],
  [5]
]

o = s.combinationSum2(input, target)
assert(len(o) == len(exp))
for x in exp:
    a = False
    for y in o:
        if match(x, y):
            a = True
    assert(a)
