import copy

class Solution:
    def wordBreak(self, s, wordDict):

        possible_outputs = []

        (words, curr, remaining) = ([], "", s)
        possible_outputs.append((words, curr, remaining))

        ans = []
        while True:
            # print(possible_outputs)
            if not possible_outputs:
                break

            words, curr, remaining = possible_outputs.pop(0)

            curr += remaining[0]
            new_remaining = remaining[1:]

            if curr in wordDict:
                new_words = copy.deepcopy(words)
                new_words.append(curr)

                if not new_remaining:
                    ans.append(new_words)
                    continue

                new_curr = ""
                possible_outputs.append((new_words, new_curr, new_remaining))

            if not new_remaining:
                continue

            possible_outputs.append((words, curr, new_remaining))

        s_ans = []
        for a in ans:
            s_ans.append(' '.join(a))

        # print(s_ans)
        return s_ans



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
