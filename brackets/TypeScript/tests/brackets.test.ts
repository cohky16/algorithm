import { solution } from "../brackets";

describe("brackets", () => {
    it("normal", () => {
        expect(solution("[]")).toEqual(true)
        expect(solution("([])")).toEqual(true)
        expect(solution("([])")).toEqual(true)
        expect(solution("}{")).toEqual(false)
        expect(solution("(]")).toEqual(false)
        expect(solution("([)]")).toEqual(false)
    })
})