function solution(arr) {
    const sum = getSum(arr);
    const length = getLength(arr);
    const answer = getAnswer(sum, length);
    return answer;
}

function getSum(arr) {
    return arr.reduce((arr, add) => arr+add, 0);
}

function getLength(arr) {
    return arr.length;
}

function getAnswer(sum, length) {
    return parseFloat(sum / length);
}