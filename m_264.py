import heapq

class Solution:
    sols = []
    window = [1,2,3]
    seen = {1: True, 2: True, 3: True}

    def nthUglyNumber(self, n: int) -> int:
        primes = [2,3,5]
        while len(self.sols) < n:
            p0 = heapq.heappop(self.window)
            for p in primes:
                new_p = p0 * p
                if new_p not in self.seen:
                    heapq.heappush(self.window, new_p)
                self.seen[new_p] = True
            self.sols.append(p0)

        print(self.sols)
        return self.sols[n-1]


        
