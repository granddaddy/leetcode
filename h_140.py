from functools import lru_cache

class Solution:
    @lru_cache(None)
    def helper(self, s):
        words = []
        if not s:
            return []

        for w in self.wordDict:
            if w == s:
                words.append(s)
                continue

            if s.startswith(w):
                others = self.helper(s[len(w):])
                for o in others:
                    words.append(w+" "+o)

        return words

    def wordBreak(self, s, wordDict):
        self.wordDict = wordDict
        return self.helper(s)


sol = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output = [
  "cats and dog",
  "cat sand dog"
]
out = sol.wordBreak(s, wordDict)
assert(len(out) == len(Output))
for k in Output:
    assert(k in out)

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output = [
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
out = sol.wordBreak(s, wordDict)
assert(len(out) == len(Output))
for k in Output:
    assert(k in out)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output = []
out = sol.wordBreak(s, wordDict)
assert(len(out) == len(Output))
for k in Output:
    assert(k in out)

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# import cProfile
# cProfile.run('sol.wordBreak(s, wordDict)')
# out = sol.wordBreak(s, wordDict)
