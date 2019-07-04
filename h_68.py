import math
class Solution:
    def build_sentence(self, str_r, n, maxWidth, last=False):
        # print(n)
        s = maxWidth - n
        t = len(str_r) - 1

        # print(str_r)
        # print(s,t)

        if last or t == 0:
            return " ".join(str_r) + " "*(s)
        else:
            q = math.floor(s/t)
            r = s - (q * t)

            # print(q,r)

            sp_0 = " "*(q+2)
            sp_1 = " "*(q+1)

            spec = sp_0.join(str_r[:r])
            if spec:
                # print(spec)
                return spec + sp_0 + sp_1.join(str_r[r:])
            return sp_1.join(str_r[r:])

    def fullJustify(self, words, maxWidth):
        ret = []
        s_r = []
        n = 0
        for word in words:
            _n = len(word)
            if n + _n + 1 > maxWidth:
                if s_r:
                    ret.append(self.build_sentence(s_r, n, maxWidth))
                s_r = [word]
                n = _n
            else:
                n += _n
                if s_r:
                    n += 1
                s_r.append(word)
        if s_r:
            ret.append(self.build_sentence(s_r, n, maxWidth, True))

        return ret
        
s = Solution()

i = ["This", "is", "an"]
assert(s.build_sentence(i, len(''.join(i))+2, 16) == "This    is    an")
i = ["example", "of", "text"]
assert(s.build_sentence(i, len(''.join(i))+2, 16) == "example  of text")
i = ["justification."]
assert(s.build_sentence(i, len(''.join(i)), 16) == "justification.  ")

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
exp = [
   "This    is    an",
   "example  of text",
   "justification.  "
]
o = s.fullJustify(words, maxWidth)
assert(exp == o)


words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
exp = [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
o = s.fullJustify(words, maxWidth)
assert(exp == o)

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
exp = [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
o = s.fullJustify(words, maxWidth)
assert(exp == o)

words = ["Listen","to","many,","speak","to","a","few."]
maxWidth = 6
exp = ["Listen","to    ","many, ","speak ","to   a","few.  "]
o = s.fullJustify(words, maxWidth)
assert(exp == o)
