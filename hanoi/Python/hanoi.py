def hanoi(n, src, dist, work):
    if n > 1:
        hanoi(n - 1, src, work, dist)
        print(n, src, "->", dist)
        hanoi(n - 1, work, dist, src)
    else:
        print(n, src, "->", dist)