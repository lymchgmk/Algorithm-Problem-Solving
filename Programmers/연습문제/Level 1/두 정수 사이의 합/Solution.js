function solution(a, b) {
    const answer = getAnswer(a, b);
    return answer;
}

function getAnswer(a, b) {
    return (a+b) * (Math.abs(a-b) + 1) / 2;
}


// TC
const a = 3;
const b = 5;
console.log(solution(a, b));
