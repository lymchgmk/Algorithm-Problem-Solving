function solution(arr) {
    const answer = getAnswer(arr);
    return answer;
}

function getAnswer(arr) {
    let lastNum = NaN;
    let answer = new Array();
    for (const num of arr) {
        if (lastNum != num) {
            answer.push(num);
            lastNum = num;
        }
    }
    return answer;
}


// TC
const arr = [1, 1, 3, 3, 0, 1, 1];
console.log(solution(arr));
