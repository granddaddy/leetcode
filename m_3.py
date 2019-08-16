def merge(a, b, vv):
    a_i = 0
    b_i = 0
    x_i = 0
    n = len(a)

    def pushdown(ai):
        l = None
        for i in range(ai, n):
            t = a[i]
            a[i] = l
            l = t

    while a_i < len(a) and b_i < len(b):
        if a[a_i] > b[b_i]:
            pushdown(a_i)
            a[a_i] = b[b_i]
            b_i += 1
        a_i += 1

    return a

a1 = [2,4,6,None,None,None]
a2 = [1,3,5]

m = merge(a1,a2, 3)
print(m)
assert(m == [1,2,3,4,5,6])
