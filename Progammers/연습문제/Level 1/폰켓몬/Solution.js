function solution(nums) {
    const pocketmons = setPocketmons(nums);
    const answer = setAnswer(nums, pocketmons);
    return answer;
}

function setPocketmons(nums) {
    return [...new Set(nums)];
}

function setAnswer(nums, pocketmons) {
    const maxPocketmons = nums.length / 2;
    const countPocketmons = pocketmons.length;
    return countPocketmons < maxPocketmons ? countPocketmons : maxPocketmons;
}


// TC
const nums = [3, 3, 3, 2, 2, 2];
console.log(solution(nums)); // 2
