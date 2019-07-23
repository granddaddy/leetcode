class Solution:
    def longestOnes(self, A, K):
        head = 0
        tail = 0

        flips_left = K

        l_seq = 0

        while tail < len(A):
            if A[tail] == 0:
                if flips_left:
                    flips_left -= 1
                else:
                    if K == 0:
                        head = tail + 1
                    else:
                        while A[head] != 0:
                            head += 1
                        head += 1

            tail += 1
            l_seq = max(l_seq, tail - head)
        return l_seq

s = Solution()
A = [0,0,1,1,1,0,0]
K = 0
assert(s.longestOnes(A, K) == 3)

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 0
assert(s.longestOnes(A, K) == 4)

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 1

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
assert(s.longestOnes(A, K) == 6)

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
assert(s.longestOnes(A, K) == 10)
