class Node:
    def __init__(self, _val,
        _prev=None, _next=None,
        _head=None, _tail=None,
        _children={}
    ):
        self.val = _val
        self.prev = _prev
        self.next = _next

        self.head = _head
        self.tail = _tail
        self.children = _children

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.d_count = {}

        self.d_count_inv = Node("d_count_inv")
        self.least_used = 2
        self.least_used_i = None

    def append_children(self, parent, child_key):
        new_child = Node(child_key)
        parent.children[child_key] = new_child

        new_child.prev = parent.tail
        if not parent.head:
             parent.head = new_child

        parent.tail = new_child
        return new_child

    def remove_children(self, parent, child_key):
        child = parent.children.pop(child_key)
        if parent.head == child:
            parent.head = child.next

        if parent.tail == child:
            parent.tail = child.prev

        if child.prev:
            child.prev.next = child.next

        if child.next:
            child.next.prev = child.prev

        return child

    def add_inv(self, _level, key):
        if _level not in self.d_count_inv.children:
            self.append_children(self.d_count_inv, _level)

        new_level = self.d_count_inv.children[_level]

        self.append_children(new_level, key)

        # update d_count_inv flags
        self.least_used = self.d_count_inv.head.head.val
        self.least_used_i = self.d_count_inv.head.val

    def remove_inv(self, _level, key):
        level = self.d_count_inv.children[_level]
        self.remove_children(level, key)

        if level.head == None and level.tail == None:
            self.remove_children(self.d_count_inv, _level)

        # update d_count_inv flags
        self.least_used = self.d_count_inv.head.head.val
        self.least_used_i = self.d_count_inv.head.val

    def evict(self):
        self.d.pop(self.least_used_i)
        self.d_count.pop(self.least_used_i)

        self.remove_inv(self.least_used, self.least_used_i)

    def update_count(self, key):
        curr_count = self.d_count.get(key, 0)
        self.d_count[key] = new_count = curr_count + 1

        # update d_count_inv
        if curr_count:
            self.remove_inv(curr_count, key)

        self.add_inv(new_count, key)

    def get(self, key: int) -> int:
        ret = self.d.get(key, -1)
        self.update_count(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if key not in self.d and len(self.d) + 1 > self.capacity:
            self.evict()

        self.d[key] = value
        self.update_count(key)

cache = LFUCache(2);

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);
cache.put(3, 3);
cache.get(2);
cache.get(3);
cache.put(4, 4);
cache.get(1);
cache.get(3);
cache.get(4);
