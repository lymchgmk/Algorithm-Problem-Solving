function solution(numbers) {
    const answer = findAnswer(numbers);
    return answer;
}

function sum(numbers) {
    let result = 0;
    for (const number of numbers) {
        result += number;
    }
    return result;
}

function findAnswer(numbers) {
    return 45 - sum(numbers);
}

// TC
const numbers = [1,2,3,4,6,7,8,0]
console.log(solution(numbers)); // 14
