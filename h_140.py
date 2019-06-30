class Solution:
    def wordBreak(self, s, wordDict):

        possible_outputs = []
        cache = {}

        (words, remaining) = ("", s)
        possible_outputs.append((words, remaining))

        ans = []
        while True:
            print(len(possible_outputs))
            if not possible_outputs:
                break

            words, remaining = possible_outputs.pop()

            if not remaining:
                if words:
                    ans.append(words)
                continue

            if remaining in cache:
                it = cache[remaining]
                cached = True
            else:
                it = wordDict
                cached = False

            c_words = []

            for i in it:
                if cached:
                    word, new_remaining = i[0], i[1]
                elif remaining.startswith(i):
                    word = i
                    new_remaining = remaining[len(word):]
                    c_words.append((word, new_remaining))
                else:
                    continue

                if words:
                    new_words = words+' '+word
                else:
                    new_words = word

                possible_outputs.append((new_words, new_remaining))

            if not cached:
                cache[remaining] = c_words

        return ans

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
out = sol.wordBreak(s, wordDict)
