import { solution } from "../pascal";

describe("pascal", () => {
    it("normal", () => {
        expect(solution(1)).toEqual([[1]])
        expect(solution(4)).toEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        expect(solution(5)).toEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
    })
})