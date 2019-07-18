class Node:
    def __init__(self, val=None, val_len=None,
                 parent=None, children=None,
                 is_word_end=False):
        self.val = val
        self.val_len = val_len
        self.parent = parent
        self.children = children
        self.is_word_end = is_word_end

class Trie:

    def __init__(self):
        self.head = Node(children={})

    def print(self):
        q = [self.head]
        while q:
            curr = q.pop()
            if curr.parent:
                print("!", curr.parent.val, curr.val, curr.is_word_end)
            else:
                print("!", curr.val)
            for c in curr.children.values():
                q.append(c)

    def insert_helper(self, curr, curr_word):
        if not curr_word:
            return False

        match = 0
        if curr.val:
            c_len = min(len(curr_word), curr.val_len)
            while match < c_len and curr_word[match] == curr.val[match]:
                match += 1

            if not match:
                return False

        rem_b = curr_word[match:]
        if match:
            rem_a = curr.val[match:]

            if not rem_a and not rem_b:
                curr.is_word_end = True
                return True

            if match < max(curr.val_len, len(curr_word)):
                m = curr.val[:match]
                n_parent = Node(m, match, curr.parent, {}, curr.is_word_end and match == curr.val_len)
                curr.parent.children.pop(curr.val)
                curr.parent.children[m] = n_parent

                if rem_a:
                    n_c_a = Node(rem_a, len(rem_a), n_parent, curr.children, curr.is_word_end)
                    for c in curr.children.values():
                        c.parent = n_c_a
                    n_parent.children[rem_a] = n_c_a
                else:
                    n_parent.children = curr.children

                curr = n_parent

        if rem_b:
            for c in curr.children.values():
                if self.insert_helper(c, rem_b):
                    return True
            if not curr.val or match:
                curr.children[rem_b] = Node(rem_b, len(rem_b), curr, {}, True)
        elif match:
            curr.is_word_end = True
        return True

    def insert(self, word: str) -> None:
        return self.insert_helper(self.head, word)

    def search_helper(self, curr, curr_word):
        if curr.val == curr_word and curr.is_word_end:
            return True

        if curr.val == curr_word[:curr.val_len]:
            curr_word = curr_word[curr.val_len:]

        for c in curr.children.values():
            if self.search_helper(c, curr_word):
                return True
        return False

    def search(self, word: str) -> bool:
        return self.search_helper(self.head, word)

    def starts_with_helper(self, curr, curr_word):
        if curr.val and curr.val.startswith(curr_word):
            return True

        if curr.val == curr_word[:curr.val_len]:
            curr_word = curr_word[curr.val_len:]

        for c in curr.children.values():
            if self.starts_with_helper(c, curr_word):
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.starts_with_helper(self.head, prefix)

trie = Trie();
trie.insert("apple");
# trie.print()
trie.insert("app");
trie.insert("apl");
trie.insert("appz");
trie.insert("bacon");
trie.print()
print(trie.search("apple"));
print(trie.search("app"));
print(trie.search("apl"));
print(trie.search("ap"));
print("###")
print(trie.startsWith("app"));
print(trie.startsWith("ap"));
print(trie.startsWith("a"));
print(trie.startsWith("ape"));
print(trie.startsWith("appp"));
