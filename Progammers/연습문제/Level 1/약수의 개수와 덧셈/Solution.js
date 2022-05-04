function solution(left, right) {
    const answer = getAnswer(left, right);
    return answer;
}

function isSquareNumber(num) {
    const root = Math.sqrt(num);
    return Number.isInteger(root);
}

function getAnswer(left, right) {
    let answer = 0;
    for (let num=left; num<=right; num++) {
        if (isSquareNumber(num)) {
            answer -= num;
        } else {
            answer += num;
        }
    }
    return answer;
}


// TC
const left = 13;
const right = 17;
console.log(solution(left, right)); // 43