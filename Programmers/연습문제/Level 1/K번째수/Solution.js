function solution(array, commands) {
    const answer = [];
    for (const command of commands) {
        const [start, end, k] = command;
        const slicedArray = sliceArray(array, start, end);
        const kthNum = getSortedKth(slicedArray, k);
        answer.push(kthNum);
    }
    return answer;
}

function sliceArray(arr, start, end) {
    return arr.slice(start-1, end);
}

function getSortedKth(arr, k) {
    arr.sort((a, b) => a - b);
    return arr[k-1];
}


// TC
const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];
console.log(solution(array, commands)); // [5, 6, 3]
