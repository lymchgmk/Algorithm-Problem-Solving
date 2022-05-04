function solution(n) {
    var answer = getAnswer(n);
    return answer;
}

function getAnswer(n) {
    const arr = String(n).split('');
    return arr.reduce((acc, curr) => acc + parseInt(curr), 0);
}