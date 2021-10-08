export class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

export var solution = (l1: ListNode, l2: ListNode): ListNode => {
    const r: ListNode[] = [];
    let t1: ListNode | null = l1;
    let t2: ListNode | null = l2;
    while (t1 || t2) {
        if (t1 && t2 && t1.val <= t2.val) {
            r.push(t1);
            t1 = t1.next;
        } else if (t2) {
            r.push(t2);
            t2 = t2.next;
        }
    }

    for (let i = r.length - 1; i > 0; i--) {
        r[i - 1].next = r[i];
    }

    return r[0];
}