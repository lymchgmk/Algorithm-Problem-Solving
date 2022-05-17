function solution(arr, divisor) {
    const answer = getAnswer(arr, divisor);
    return answer;
}

function getAnswer(arr, divisor) {
    const answer = arr.filter(num => num % divisor === 0);
    return answer.length === 0 ? [-1] : answer.sort((a, b) => a-b);
}


// TC
const arr = [5, 9, 7, 10];
const divisor = 5;
console.log(solution(arr, divisor));
