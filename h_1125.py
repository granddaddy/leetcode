class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills_d = {}
        for i, skill in enumerate(req_skills):
            skills_d[skill] = i

        M = len(req_skills)
        MM = (1 << M) - 1

        ppl = []
        for i, p in enumerate(people):
            p_s = 0
            for skill in p:
                p_s |= 1 << skills_d[skill]

            ppl.append((1 << i, p_s))

        n_ppl = len(people)
        rem_l = {}
        for i in range(n_ppl):
            for j in range(i+1, n_ppl):
                _i = ppl[i][1]
                _j = ppl[j][1]
                if not _i:
                    rem_l[i] = True
                    break
                _ij = _i & _j
                if _ij == i:
                    rem_l[j] = True
                elif _ij == j:
                    rem_l[i] = True
        ppl2 = []
        for i in range(n_ppl):
            if i not in rem_l:
                ppl2.append(ppl[i])

        ret = 0

        while True:
            ii, p2 = ppl2.pop(0)
            if p2 == MM:
                ret = ii
                break
            for i, _p in ppl:
                if ii & i == i:
                    continue
                s = p2 | _p
                if s == MM:
                    ii |= i
                    ret = ii
                    break
                else:
                    _ii = ii
                    _ii |= i
                    ppl2.append((_ii, s))
            if ret:
                break

        ret_arr = []
        for i in range(n_ppl):
            if ret & 1 == 1:
                ret_arr.append(i)
            ret = ret >> 1

        return ret_arr
            
