export var solution = (x: number): boolean => {
    const s = String(x)
    return s.split('').reverse().join('') == s
};