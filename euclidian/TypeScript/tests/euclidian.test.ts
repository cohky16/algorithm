import { solution } from "../euclidian";

describe("euclidian", () => {
    it("normal", () => {
        expect(solution(12, 15)).toEqual(3)
        expect(solution(20, 15)).toEqual(5)
        expect(solution(542, 984)).toEqual(2)
    })
})