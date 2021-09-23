export var solution = (s: string): boolean => {
    const o = ['(',  ')', '{', '}', '[', ']']
    const l = s.length
    for (let i = 0; i < l / 2; i++) if (o.indexOf(s[i]) + 1 != o.indexOf(s[l - 1 - i])) return false
    return true
};