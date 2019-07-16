class Solution:
    def lengthLongestPath(self, str):
        stack = []
        len_stack = [-1]
        m = 0

        last_level = 0
        for l in str.split("\n"):
            tabs = 0
            while l[tabs] == "\t":
                tabs += 1

            diff = last_level - tabs
            if stack and diff >= 0:
                for i in range(diff + 1):
                    stack.pop()
                    len_stack.pop()

            stack.append(l[tabs:])
            new_val = len_stack[-1] + 1 + len(l[tabs:])
            len_stack.append(new_val)

            if '.' in l:
                m = max(new_val, m)

            last_level = tabs
            # print(stack)

        return m

s = Solution()
o = s.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
print(o)
assert(o == 20)
o = s.lengthLongestPath("a")
print(o)
assert(o == 0)
