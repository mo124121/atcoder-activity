def insertion_sort(a: list):
    n = len(a)
    for i in range(n):
        v = a[i]
        j = i
        while j > 0:
            if a[j - 1] > v:
                a[j] = a[j - 1]
            else:
                break
            j -= 1
        a[j] = v


def merge_sort(a: list, l: int, r: int):
    if r - l == 1:
        return
    m = (r + l) // 2
    merge_sort(a, l, m)
    merge_sort(a, m, r)

    buf = []
    for i in range(l, m):
        buf.append(a[i])
    for i in range(r - 1, m - 1, -1):
        buf.append(a[i])

    i_l = 0
    i_r = len(buf) - 1
    for i in range(l, r):
        if buf[i_l] <= buf[i_r]:
            a[i] = buf[i_l]
            i_l += 1
        else:
            a[i] = buf[i_r]
            i_r -= 1


def quick_sort(a: list, l: int, r: int):
    if r - l <= 1:
        return

    p_i = (r + l) // 2  # 中点
    p = a[p_i]

    a[p_i], a[r - 1] = a[r - 1], a[p_i]
    i = l
    for j in range(l, r - 1):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r - 1] = a[r - 1], a[i]

    quick_sort(a, l, i)
    quick_sort(a, i + 1, r)


def bucket_sort(a: list):
    n = max(a)
    count = [0] * (n + 1)
    for ai in a:
        count[ai] += 1
    ret = []
    for i, c in enumerate(count):
        ret.extend([i] * c)
    return ret


if __name__ == "__main__":
    b = [1, 1515, 3314, 134, 35]
    quick_sort(b, 0, len(b))
    print(b)
    c = [114, 114, 2, 55, 11135, 42]
    print(bucket_sort(c))
