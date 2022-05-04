function solution(n) {
    const answer = getAnswer(n);
    return answer;
}

function getAnswer(n) {
    return String(n).split('').reverse().map(a => parseInt(a));
}