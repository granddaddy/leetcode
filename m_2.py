class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def get_tail(num):
    t = None
    d = num
    while True:
        d.prev = t
        t = d
        if d.next:
            d = d.next
        else:
            break

    return d

def add(num1, num2):
    t1 = get_tail(num1)
    t2 = get_tail(num2)

    ret = None

    carry = 0
    while True:
        if t1 == None and t2 == None:
            return ret

        _t1 = 0 if t1 == None else t1.val
        _t2 = 0 if t2 == None else t2.val

        s = _t1 + _t2 + carry
        if s >= 10:
            carry = 1
            s -= 10
        else:
            carry = 0

        r = Node(s, ret)
        ret = r

        if t1:
            t1 = t1.prev
        if t2:
            t2 = t2.prev

n1 = Node(1, Node(2, Node(3)))
n2 = Node(4, Node(5, Node(6)))

o = add(n1, n2)
_o = ""
while True:
    if o:
        _o += str(o.val)
        o = o.next
    else:
        break
print(_o)
assert(int(_o) == 579)

n1 = Node(5, Node(9, Node(2, Node(3))))
n2 = Node(4, Node(5, Node(6)))

o = add(n1, n2)
_o = ""
while True:
    if o:
        _o += str(o.val)
        o = o.next
    else:
        break
print(_o)
assert(int(_o) == 6379)
