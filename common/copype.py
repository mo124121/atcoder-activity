import sys

sys.setrecursionlimit(10**6)

if sys.implementation.name == "pypy":
    import pypyjit

    pypyjit.set_param("max_unroll_recursion=-1")


class LinkedList:
    class Cell:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self, *args):
        self.nil = LinkedList.Cell(None)
        self.nil.next = self.nil
        for x in reversed(args):
            self.insert(x)

    def __del__(self):
        self.nil.next = None

    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n:
                return cp
            i += 1
            cp = cp.link
        return None

    def at(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        return None

    def insert(self, v, p=None):
        if p is None:
            p = self.nil
        v.next = p.next
        p.next = v

    def push(self, value):
        data = LinkedList.Cell(value)
        self.insert(data)

    def print_list(self):
        cur = self.nil.next
        while cur != self.nil:
            print(cur.data, "-> ", end="")
            cur = cur.next
        print("")


def change_base(value: int, base: int):
    if int(value / base):
        return change_base(int(value / base), base) + str(value % base)
    return str(value % base)


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def tousa_sum(a, d, n):
    # 初項a,交差d,項数n
    return n * (2 * a + (n - 1) * d) // 2


##復元できるの
def compress(L):
    S = sorted(set(L))  # 配列に含まれるユニークな要素
    d = dict()  # 要素の順位
    i = 0
    for s in S:
        d[s] = i
        i += 1
    return i, S, d


n, S, d = compress(L)

# 復元できないもの
def compress(L):
    S = sorted(set(L))  # 配列に含まれるユニークな要素
    d = dict()  # 要素の順位
    i = 0
    for s in S:
        d[s] = i
        i += 1
    ret = []
    for l in L:
        ret.append(d[l])

    return ret


if __name__ == "__main__":
    linkedlist = LinkedList()

    names = ["satoshi", "kakeru", "sho", "kiyoshi", "goro"]

    for name in names:
        linkedlist.push(name)

    linkedlist.print_list()
    del linkedlist
