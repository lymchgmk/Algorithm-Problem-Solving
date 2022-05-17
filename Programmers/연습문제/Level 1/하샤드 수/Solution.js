function solution(x) {
    var answer = getIsHarshad(x);
    return answer;
}

function getIsHarshad(x) {
    const digitSum = String(x).split('').reduce((acc, add) => acc + parseInt(add));
    return Boolean(x % digitSum === 0);
}