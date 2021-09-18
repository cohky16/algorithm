 export var solution = (n: number): number => {
    if (n < 0) return 0;
    if (n == 0) return 1;
    return solution(n - 1) + solution(n - 2)
}
