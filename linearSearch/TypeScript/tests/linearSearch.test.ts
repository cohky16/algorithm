import { solution } from "../linearSearch";

describe("linearSearch", () => {
    it("normal", () => {
        expect(solution([1, 3, 7, 4], 7)).toEqual([1, 3])
        expect(solution([1, 3, 4, 7, 5], 10)).toEqual([1, 3])
    })
})