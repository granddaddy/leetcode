import random

def rand7():
    return random.randint(1,7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()

        while True:
            if b == 1 or b <= 4 and a == 7:
                return a + b - 1
            a = rand7()
            b = rand7()



s = Solution()
a = []
for i in range(10000):
    a.append(s.rand10())
a.sort()
print(a)

last = None
count = 0
for i in a:
    if i != last:
        print(last, count)
        last = i
        count = 1
    else:
        count += 1

print(last, count)
