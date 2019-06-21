import math
import copy

MAX_INT = int("9" * 19)

def is_odd(n):
    if n % 2 == 1:
        return True
    return False

def get_mid(n):
    return math.ceil(n/2)

def reverse_str(s):
    return s[::-1]

def is_palindrome(n):
    n_len = len(n)
    mid = get_mid(n_len)
    mid_index = mid - 1

    if is_odd(n_len):
        n_0 = n[:mid_index] + n[mid_index] + reverse_str(n[:mid_index])
    else:
        n_0 = n[:mid_index+1] + reverse_str(n[:mid_index+1])

    if n_0 == n:
        return True
    return False

def is_sol(n):
    if n >= 0 and is_palindrome(str(n)):
        return True
    return False

def y(n):
    i = 1
    int_n = int(n)

    while True:
        neg = int_n - i
        pos = int_n + i

        if is_sol(neg):
            return str(neg)
        if is_sol(pos):
            return str(pos)

        i = i + 1

def closest_one_more_digit(n_len):
    return int("1" + ("0" * (n_len - 1)) + "1")

def closest_one_less_digit(n_len):
    if n_len == 1:
        return MAX_INT

    return int("9" * (n_len - 1))

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def head(a,b):
    return a

def closest_same_digits(n):
    return (int(closest_same_digits_h(n, head)), int(closest_same_digits_h(n, add)), int(closest_same_digits_h(n, sub)))

def closest_same_digits_h_old(n, f):
    n_len = len(n)
    mid = get_mid(n_len)
    mid_index = mid - 1

    if is_odd(n_len):
        n_0 = n[:mid_index] + n[mid_index] + reverse_str(n[:mid_index])
    else:
        n_0 = n[:mid_index+1] + reverse_str(n[:mid_index+1])

    n_1 = list(n_0)

    mid = n[mid_index]
    new_mid = str(max(0,f(int(mid),1)))

    if is_odd(n_len):
        n_1[mid_index] = new_mid
    else:
        n_1[mid_index] = new_mid
        n_1[mid_index+1] = new_mid

    return ''.join(n_1)

def closest_same_digits_h(n, f):
    n_len = len(n)
    mid = get_mid(n_len)
    mid_index = mid - 1

    if is_odd(n_len):
        n_0 = n[:mid_index] + n[mid_index] + reverse_str(n[:mid_index])
    else:
        n_0 = n[:mid_index+1] + reverse_str(n[:mid_index+1])

    n_1 = list(n_0)

    mid = n[mid_index]
    new_mid = str(max(0,f(int(mid),1)))

    if is_odd(n_len):
        n_1[mid_index] = new_mid
    else:
        n_1[mid_index] = new_mid
        n_1[mid_index+1] = new_mid

    return ''.join(n_1)
    
assert(closest_same_digits_h("101", sub) == "111")
assert(closest_same_digits_h("121", sub) == "111")
assert(closest_same_digits_h("1111", sub) == "1001")
assert(closest_same_digits_h("1221", sub) == "1111")
assert(closest_same_digits_h("89023482", head) == "89022098")
print(closest_same_digits_h("06", head))
assert(closest_same_digits_h("06", head) == "00")
assert(closest_same_digits_h("1283", add) == "1331")

def d(a, b):
    return abs(a-b)

def it_method(n):
    n_len = len(n)
    mid = get_mid(n_len)
    mid_index = mid - 1

    if n_len < 2:
        return MAX_INT

    if is_odd(n_len):
        n_0 = n[:mid_index] + n[mid_index] + reverse_str(n[:mid_index])
    else:
        n_0 = n[:mid_index+1] + reverse_str(n[:mid_index+1])

def x(n):
    int_n = int(n)
    n_len = len(n)
    mid = get_mid(n_len)
    mid_index = mid - 1

    ll = []
    ll.append(closest_one_more_digit(n_len))
    ll.append(closest_one_less_digit(n_len))
    ll.extend(closest_same_digits(n))

    all = sorted(ll)
    all = list(filter(lambda x: x != int_n, all))

    d_arr = list(map(lambda x: d(x, int_n),all))
    min_d = min(d_arr)

    return str(all[d_arr.index(min_d)])


assert(closest_one_more_digit(1) == 11)
assert(closest_one_more_digit(2) == 101)
assert(closest_one_less_digit(2) == 9)
assert(closest_one_less_digit(3) == 99)
assert(closest_one_more_digit(1) == 11)
assert(closest_one_more_digit(2) == 101)

assert(is_palindrome("121") == True)
assert(is_palindrome("123") == False)
assert(is_palindrome("1221") == True)
assert(is_palindrome("1223") == False)
assert(is_palindrome("1") == True)

assert(is_odd(0) == False)
assert(is_odd(1) == True)
assert(is_odd(2) == False)

assert(get_mid(7) == 4)
assert(get_mid(4) == 2)

assert(reverse_str("123") == "321")

assert(x("1") == "0")
assert(x("8") == "7")
assert(x("10") == "9")
assert(x("89023482") == "89022098")
assert(x("1283") == "1331")
# assert(x("1325060231") == "1325005231")
