export var solution = (nums: number[], target: number): number[] => {
    const list: number[] = [];

    for (let i = 0; i < nums.length; i++){
        const p = list.indexOf(target - nums[i])
        if (p > 0) return [p, i];
        list[i] = nums[i];
    }
    
    return [-1, -1];
};