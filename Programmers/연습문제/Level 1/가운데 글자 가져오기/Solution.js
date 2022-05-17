function solution(s) {
    const answer = getMiddleChar(s);
    return answer;
}

function getMiddleChar(s) {
    const start = Math.ceil(s.length / 2) - 1;
    const length = s.length % 2 ? 1 : 2;
    return s.substr(start, length);
}


// TC
const s = "qwer";
console.log(solution(s)); // "we"
