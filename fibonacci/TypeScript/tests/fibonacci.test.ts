import { solution } from "../fibonacci"

describe("fibonacci", () => {
    it("normal", () => {
        expect(solution(2)).toEqual(2);
        expect(solution(3)).toEqual(3);
        expect(solution(4)).toEqual(5);
        expect(solution(5)).toEqual(8);
        expect(solution(6)).toEqual(13);
        expect(solution(40)).toEqual(165580141);
    })
})
