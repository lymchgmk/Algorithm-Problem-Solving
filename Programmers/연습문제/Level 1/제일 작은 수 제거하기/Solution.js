function solution(arr) {
    const min = getMinNum(arr);
    const answer = getAnswer(arr, min);
    return answer;
}

function getMinNum(arr) {
    let min = Infinity;
    for (const num of arr) {
        if (min > num) {
            min = num;
        }
    }
    return min;
}

function getAnswer(arr, min) {
    let answer = [];
    for (const num of arr) {
        if (num != min) {
            answer.push(num);
        }
    }
    return answer.length === 0 ? [-1] : answer;
}