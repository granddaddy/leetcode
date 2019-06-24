import heapq
ON_INCLINE = "on_incline"
ON_DECLINE = "on_decline"
ON_FLAT = "on_decline"

class Solution:
    def set_dir_flag(self, flag):
        if flag == ON_INCLINE:
            self.on_incline = True
            self.on_decline = False
        elif flag == ON_DECLINE:
            self.on_incline = False
            self.on_decline = True
        else:
            raise

    def get_curr_dir(self):
        if self.on_incline and not self.on_decline:
            return ON_INCLINE
        if self.on_decline and not self.on_incline:
            return ON_DECLINE
        else:
            raise

    def reset_dir_flag(self):
        self.on_decline = False
        self.on_incline = False

    def reset_ds(self):
        self.potential_lefts = []
        self.potential_rights = []
        self.all = []

    def add_right(self, h, index):
        self.potential_rights.append((h, index))
        self.all.append((h, index))

    def add_left(self, h, index):
        self.potential_lefts.append((h, index))
        self.all.append((h, index))

    def fill_water(self, height):
        # print(self.potential_lefts)
        # print(self.potential_rights)
        if len(self.potential_lefts) == 0:
            return 0

        if len(self.potential_rights) == 0:
            return 0

        t = 0
        left = self.potential_lefts[0][0]
        right = self.potential_rights[-1][0]

        m = min(left, right)

        for h, i in self.potential_lefts:
            if h < m:
                t += m - h
                height[i] = m

        for h, i in self.potential_rights:
            if h < m:
                t += m - h
                height[i] = m

        return t

    def get_dir(self, last, curr):
        if last < curr:
            new_dir = ON_INCLINE
        elif last > curr:
            new_dir = ON_DECLINE
        else:
            new_dir = ON_FLAT

        return new_dir

    # def trap(self, height: List[int]) -> int:
    def trap(self, height) -> int:
        total = 0
        while True:
            t = self.trap_helper(height)
            total += t
            if t == 0:
                break

        return total

    def trap_helper(self, height) -> int:
        total = 0
        index = 0

        self.reset_dir_flag()
        self.reset_ds()

        while True:
            if index >= len(height):
                total += self.fill_water(height)
                break

            curr = height[index]

            if len(self.all) == 0:
                self.add_right(curr, index)
                self.set_dir_flag(ON_INCLINE)
                index += 1
                continue

            last = self.all[-1][0]
            new_dir = self.get_dir(last, curr)
            curr_dir = self.get_curr_dir()
            # print(last, curr_dir)
            # print(curr, index, new_dir)

            if curr_dir == ON_DECLINE:
                if new_dir == ON_INCLINE:
                    self.add_right(curr, index)
                    self.set_dir_flag(new_dir)
                else:
                    self.add_left(curr, index)
            elif curr_dir == ON_INCLINE:
                if new_dir == ON_DECLINE:
                    total += self.fill_water(height)
                    l = self.potential_rights[-1]
                    self.reset_ds()

                    self.add_left(*l)
                    self.set_dir_flag(new_dir)
                    continue
                else:
                    self.add_right(curr, index)
            else:
                self.add_left(curr, index)
                if new_dir != ON_FLAT:
                    self.set_dir_flag(new_dir)

            index += 1

        return total

s = Solution()
assert(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
