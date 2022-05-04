function solution(s) {
    const answer = getSorted(s);
    return answer;
}

function getSorted(s) {
    return Array.from(s).sort().reverse().join('');
}