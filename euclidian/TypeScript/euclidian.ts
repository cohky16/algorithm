export var solution = (a: number, b:number): number => {
    let r = 0
    while (b != 0) {
        r = a % b
        a = b
        b = r
    }
    return a
};