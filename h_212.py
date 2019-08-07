class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = []

        if not board or not words:
            return ret

        N = len(board)
        M = len(board[0])

        dirs = [
                (-1,0),
                (0,-1), (0,1),
                (1,0)
               ]

        words_d = {}

        for w in words:
            l = words_d.get(w[0], [])
            words_d[w[0]] = l
            l.append(w)

        def in_board(i, j):
            if 0 <= i and i < N:
                if 0 <= j and j < M:
                    return True
            return False

        def find(s_i, s_j, poss_words):
            f_words = []

            def traverse(i, l_d, pw, curr, visited):
                l_i, l_j, _ = curr[i-1]
                for di in range(l_d + 1, len(dirs)):
                    pd = dirs[di]
                    i_m = pd[0]
                    j_m = pd[1]

                    n_i = l_i + i_m
                    n_j = l_j + j_m

                    if (n_i, n_j) not in visited and \
                        in_board(n_i, n_j) and \
                        board[n_i][n_j] == pw[i]:
                        return (n_i, n_j, di)

                return None

            for pw in poss_words:
                curr = [(s_i, s_j, 0), (-1, -1, -1)]
                visited = {(s_i, s_j): True}
                n = len(pw)
                if n == 1:
                    f_words.append(pw)
                    continue
                i = 1
                while True:
                    if i == 0:
                        break

                    lc = curr[i]
                    ld = lc[2]
                    if ld != -1:
                        visited.pop((lc[0],lc[1]))

                    pt = traverse(i, ld, pw, curr, visited)
                    if pt:
                        visited[(pt[0], pt[1])] = True
                    curr[i] = pt

                    if not pt:
                        i -= 1
                        lt = curr.pop()

                    elif i < n - 1:
                        i += 1
                        curr.append((-1,-1,-1))
                        continue

                    elif i == n - 1:
                        f_words.append(pw)
                        break

            return f_words

        for i in range(N):
            for j in range(M):
                l = board[i][j]
                if l in words_d:
                    poss_words = words_d[l]
                    _find = find(i, j, poss_words)
                    if _find:
                        for fw in _find:
                            poss_words.remove(fw)
                        if not poss_words:
                            words_d.pop(l)
                        ret.extend(_find)

        return ret
