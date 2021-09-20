import { solution } from "../palindromic";

describe("palindromic", () => {
    it("normal", () => {
        expect(solution(101)).toEqual(true)
        expect(solution(202)).toEqual(true)
        expect(solution(123454321)).toEqual(true)
        expect(solution(-101)).toEqual(false)
    })
})