function solution(x, n) {
    var answer = getAnswer(x, n);
    return answer;
}

function getAnswer(x, n) {
    const answer = [];
    let num = x;
    while (answer.length < n) {
        answer.push(num);
        num += x;
    }
    return answer;
}