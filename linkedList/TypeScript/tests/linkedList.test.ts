import { ListNode, solution } from "../linkedList";

describe("linkedList", () => {
    it("normal", () => {
        const t1 = new ListNode();
        t1.val = 1;
        t1.next = new ListNode();
        t1.next.val = 3;
        t1.next.next = new ListNode();
        t1.next.next.val = 5;
        t1.next.next.next = null;
        
        const t2 = new ListNode();
        t2.val = 2;
        t2.next = new ListNode();
        t2.next.val = 4;
        t2.next.next = new ListNode();
        t2.next.next.val = 6;
        t2.next.next.next = null;

        let ts = solution(t1, t2);
        let count = 1;
        while(ts.next) {
            expect(ts.val).toEqual(count++);
            ts = ts.next;
        }
    })
})