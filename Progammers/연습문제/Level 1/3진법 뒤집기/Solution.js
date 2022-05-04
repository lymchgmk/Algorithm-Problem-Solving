function solution(n) {
    const ternary = getTernary(n);
    const reversedTernary = getReversed(ternary);
    const answer = getDecimal(reversedTernary);
    return answer;
}

function getTernary(n) {
    return n.toString(3);
}

function getReversed(str) {
    return str.split('').reverse().join('');
}

function getDecimal(str) {
    return parseInt(str, 3);
}


// TC
const n = 45;
console.log(solution(n));
