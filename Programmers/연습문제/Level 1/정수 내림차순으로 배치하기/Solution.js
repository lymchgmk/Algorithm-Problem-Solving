function solution(n) {
    const arr = getArr(n);
    const sortedArr = getSorted(arr);
    const answer = getAnswer(sortedArr);
    return answer;
}

function getArr(n) {
    return String(n).split('');
}

function getSorted(arr) {
    return arr.sort((a, b) => (b-a));
}

function getAnswer(arr) {
    const result = arr.map(a => String(a)).join('');
    return parseInt(result);
}