export var solution = (n: number): number => {
    let m: number[] = []
    m[0] = 1, m[1] = 1
    for (let i = 2; i <= n; i++) m[i] = m[i - 1] + m[i - 2]
    return m[n]
}
