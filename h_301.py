from functools import lru_cache
parens = ['(', ')']
len_parens = len(parens)

@lru_cache(None)
def is_valid(s):
    st = []
    for l in s:
        if l == parens[1]:
            if st and st[-1] == parens[0]:
                st.pop()
            else:
                st.append(l)
        if l == parens[0]:
            st.append(l)

    if not st:
        return True
    return False

class Solution:
    def removeInvalidParentheses(self, s: str):
        if is_valid(s):
            return [s]

        p = [(s, len(s))]
        visited = {}
        ans = []
        n = None
        while True:
            if not p:
                break
            _s, _n = p.pop(0)
            if _s in visited:
                continue
            else:
                visited[_s] = True
            if is_valid(_s):
                if not n:
                    n = _n
                else:
                    if _n < n:
                        break

                ans.append(_s)

            for i in range(0, _n):
                l = _s[:i]
                r = _s[i+1:]
                p.append((l+r, _n-1))

        # print(n)
        # print(ans)
        return ans



s = Solution()
samp = ["()()(a)", "(())a()", ""]
for ss in samp:
    assert(is_valid(ss))
assert(is_valid("()())(") == False)

input = ""
out = [""]
o = s.removeInvalidParentheses(input)
assert(len(o) == len(out))
for x in o:
    assert(x in out)

input = "()())()"
out = ["()()()", "(())()"]
o = s.removeInvalidParentheses(input)
assert(len(o) == len(out))
for x in o:
    assert(x in out)

input = "(a)())()"
out = ["(a)()()", "(a())()"]
o = s.removeInvalidParentheses(input)
assert(len(o) == len(out))
for x in o:
    assert(x in out)

input = ")("
out = [""]
o = s.removeInvalidParentheses(input)
assert(len(o) == len(out))
for x in o:
    assert(x in out)

import cProfile
cProfile.run('s.removeInvalidParentheses(")()()i)())b(())h))))")')
