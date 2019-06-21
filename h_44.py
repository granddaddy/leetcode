AS = "*"
QU = "?"

def is_wildcard(s):
    return s == AS or s == QU

def is_empty(s):
    return len(s) == 0

def get_first_elem(s):
    try:
        return s[0]
    except:
        return None

def x(pattern,string):
    return y(string,pattern)

def y(s,p):

    sols = []
    sols.append((s,p))

    while True:
        if len(sols) == 0:
            return False

        s_0, p_0 = sols.pop(0)

        if s_0 == p_0:
            return True

        s_f = get_first_elem(s_0)
        p_f = get_first_elem(p_0)

        if p_f == None:
            continue

        elif not is_wildcard(p_f):
            if s_f == p_f:
                if is_empty(s_0[1:]) and is_empty(p_0[1:]):
                    return True
                else:
                    sols.append((s_0[1:], p_0[1:]))
                    continue
            else:
                continue

        else:
            if p_f == QU:
                sols.append((s_0[1:], p_0[1:]))
                continue

            else:
                # zero case
                sols.append((s_0, p_0[1:]))
                # one case
                sols.append((s_0[1:], p_0))
                print(sols)
                continue

assert(x("a", "a") == True)
assert(x("a*", "abc") == True)
assert(x("a*", "a") == True)
assert(x("a*", "ab") == True)
assert(x("a*c", "abbbbbbc") == True)
assert(x("a*b", "abbbbbbb") == True)

assert(x("a*", "b") == False)

assert(x("a?c", "abc") == True)
assert(x("a?c", "abd") == False)
assert(x("a?c", "abcd") == False)
assert(x("a*c?b", "acdcb") == False)
