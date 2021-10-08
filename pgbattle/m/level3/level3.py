def main():
    n, m = map(int, input().split())
    h = 0
    p = [1]*m
    for i in range(n):
        c = sum(map(int, input().split()))
        if i >= c and p[c] == 1:
            h += 1
            p[c + 1] = 0
        p[i] = 0
    print(h)