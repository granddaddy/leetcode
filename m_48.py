class Solution:
    def get_side(self, side, i, n=None):
        if not n:
            n = self.n
        if side == 0:
            return map(lambda x: (i, x), range(i, n-i))
        if side == 1:
            return map(lambda x: (x, n-1-i), range(i, n-i))
        if side == 2:
            return map(lambda x: (n-1-i, x), reversed(range(i, n-i)))
        if side == 3:
            return map(lambda x: (x, i), reversed(range(i, n-i)))

    def rotate(self, matrix):
        self.n = len(matrix[0])
        i = 0

        while True:
            r = self.n - (i*2)
            if r <= 1:
                break

            s0 = self.get_side(0, i)
            s1 = self.get_side(1, i)
            s2 = self.get_side(2, i)
            s3 = self.get_side(3, i)

            sides = [s0, s1, s2, s3]

            for j in range(r-1):
                a = next(sides[0])
                for k in range(1,4):
                    b = next(sides[k])
                    t = matrix[b[0]][b[1]]
                    matrix[b[0]][b[1]] = matrix[a[0]][a[1]]
                    matrix[a[0]][a[1]] = t

            i += 1

s = Solution()

assert(list(s.get_side(0, 0, 4)) == [(0,0),(0,1),(0,2),(0,3)])
assert(list(s.get_side(1, 0, 4)) == [(0,3),(1,3),(2,3),(3,3)])
assert(list(s.get_side(2, 0, 4)) == [(3,3),(3,2),(3,1),(3,0)])
assert(list(s.get_side(3, 0, 4)) == [(3,0),(2,0),(1,0),(0,0)])

assert(list(s.get_side(0, 1, 4)) == [(1,1),(1,2)])
assert(list(s.get_side(1, 1, 4)) == [(1,2),(2,2)])
assert(list(s.get_side(2, 1, 4)) == [(2,2),(2,1)])
assert(list(s.get_side(3, 1, 4)) == [(2,1),(1,1)])

a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
o = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

assert(o != a)
s.rotate(a)
assert(o == a)

a = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
o = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

assert(o != a)
s.rotate(a)
assert(o == a)
