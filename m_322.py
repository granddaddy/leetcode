from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def _coinChange(self, amount):
        mn = float('inf')
        for c in self.coins:
            if c == amount:
                return 1
            if c < amount:
                _c = self._coinChange(amount - c)
                mn = min(mn, 1 + _c)

        return mn
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        coins.sort(reverse=True)
        self.coins = coins
        
        ret = self._coinChange(amount)
        if ret == float('inf'):
            return -1
        return ret
