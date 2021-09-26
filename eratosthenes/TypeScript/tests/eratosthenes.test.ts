import { solution } from "../eratosthenes";

describe("eratosthenes", () => {
    it("normal", () => {
        expect(solution(100)).toEqual(25)
        expect(solution(120)).toEqual(30)
    })
})