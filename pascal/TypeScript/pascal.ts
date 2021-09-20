export var solution = (numRows: number): number[][] => {
    const r: number[][] = []
    for (let i = 0; i < numRows; i++) {
        const t: number[] = []
        for (let j = 0; j <= i; j++) {
            if (j == 0 || i == j) t.push(1)
            else {
                const p = r[i - 1]
                t.push(p[j] + p[j - 1])
            }
        }
        r.push(t)
    }
    return r
};