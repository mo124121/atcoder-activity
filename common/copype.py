import sys  # 追加

sys.setrecursionlimit(500 * 500)  # 追加


class UnionFind:
    def __init__(self, N):

        self.parent = [0] * N
        for i in range(N):
            self.parent[i] = i

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent = self.root(self.parent[x])
            return self.parent

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        else:
            self.parent[root_x] = root_y

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y


import gc


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


if __name__ == "__main__":
    linkedlist = LinkedList()

    names = ["satoshi", "kakeru", "sho", "kiyoshi", "goro"]

    for name in names:
        linkedlist.push(name)

    linkedlist.print_list()
    del linkedlist
