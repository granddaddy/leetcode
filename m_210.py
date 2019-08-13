class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        poss_starts = {}
        reqs = {}
        edges = {}

        for i in range(numCourses):
            poss_starts[i] = True

        for p in prerequisites:
            h = p[0]
            t = p[1]

            poss_starts.pop(h, None)

            e = reqs.setdefault(h, {})
            e[t] = True

            e = edges.setdefault(t, [])
            e.append(h)

        q = []
        curr = []

        for ps in poss_starts.keys():
            q.append(ps)
            curr.append(ps)

        while True:
            if not q:
                break

            n = q.pop()

            for m in edges.get(n, []):
                m_r = reqs.get(m, {})
                m_r.pop(n)
                if not m_r:
                    q.append(m)
                    curr.append(m)

        if len(curr) < numCourses:
            return []

        return curr
