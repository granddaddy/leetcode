import threading
def printNumber(int):
    print(int)
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.end = 2*n
        self.curr = 0
        self.l = lock = threading.Lock()


	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        while self.curr < self.end - 1:
            with self.l:
                if self.curr % 2 == 0:
                    printNumber(0)
                    self.curr += 1

    def even(self, printNumber):
        num = 2
        while self.curr < self.end:
            with self.l:
                if self.curr % 4 == 3:
                    printNumber(num)
                    num += 2
                    self.curr += 1

    def odd(self, printNumber):
        num = 1
        while self.curr < self.end:
            if self.curr % 4 == 1:
                printNumber(num)
                num += 2
                self.curr += 1

z = ZeroEvenOdd(40)
t = [
    threading.Thread(target=z.zero, args=(printNumber,)),
    threading.Thread(target=z.even, args=(printNumber,)),
    threading.Thread(target=z.odd, args=(printNumber,))
]

for _t in t:
    _t.start()

for _t in t:
    _t.join()
