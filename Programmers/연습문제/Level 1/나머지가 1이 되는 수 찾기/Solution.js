function solution(n) {
    const answer = getAnswer(n);
    return answer;
}

function getAnswer(n) {
    for (let x=2; x<n; x++) {
        if (n % x == 1) {
            return x;
        }
    }
}


// TC
const n = 10;
console.log(solution(n)); // 3
