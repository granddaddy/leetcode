class Node:
    def __init__(self, val=None,
                l_child=None, r_child=None,
                 lefts=None, rights=None):
        self.val = val

        self.l_child = l_child
        self.r_child = r_child

        self.lefts = lefts if lefts else []
        self.rights = rights if rights else []

    def __bool__(self):
        return bool(self.val)

class MyCalendar:

    def __init__(self):
        self.root = Node()

    def book(self, start: int, end: int) -> bool:
        # print("\n","s",start,end)
        curr_node = self.root
        m = (start+end)/2

        while True:
            # print("curr",curr_node.val)
            if not curr_node:
                curr_node.val = m
                curr_node.lefts = [(start)]
                curr_node.rights = [(end)]
                # print("set",curr_node.val)
                return True

            curr_val = curr_node.val
            if curr_val < start:
                for e in curr_node.rights:
                    if start < e:
                        return False

                # print("r")
                if not curr_node.r_child:
                    curr_node.r_child = Node()
                curr_node = curr_node.r_child

            elif end < curr_val:
                for s in curr_node.lefts:
                    if s < end:
                        return False

                # print("l")
                if not curr_node.l_child:
                    curr_node.l_child = Node()
                curr_node = curr_node.l_child

            else:
                return False

# obj = MyCalendar()
# print(obj.book(10,20))
# print(obj.book(15,25))
# print(obj.book(20,30))

obj = MyCalendar()
t_cases = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
for t in t_cases:
    print(obj.book(*t))
