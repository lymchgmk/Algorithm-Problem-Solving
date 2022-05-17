function solution(strings, n) {
    const answer = getAnswer(strings, n);
    return answer;
}

function getAnswer(strings, n) {
    return strings.sort(
        (a, b) => a[n] === b[n] ? a.localeCompare(b) : a[n].localeCompare(b[n])
    )
}


// TC
const strings = ["abce", "abcd", "cdx"];
const n = 2;
console.log(solution(strings, n));