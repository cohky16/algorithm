export var solution = (x: number): number => {
    let l = [...Array(x)].map((_) => true)
    l[0] = false
    for (let i = 2; i <= x**0.5; i++) if (l[i - 1] == true) for (let j = i * 2; j <= x; j += i) l[j - 1] = false
    return l.filter((n) => n).length
};