def main():
    w, k, d = map(int, input().split())
    print("Yes") if max(k, w-k) <= d else print("No")