function solution(numbers) {
    const answer = getAnswer(numbers);
    return answer;
}

function getAnswer(numbers) {
    let answer = new Set();
    for (let i=0; i<numbers.length; i++) {
        for (let j=0; j<numbers.length; j++) {
            if (i != j) {
                answer.add(numbers[i]+numbers[j]);
            }
        }
    }
    answer = sorted(Array.from(answer));
    return answer;
}

function sorted(arr) {
    return arr.sort((a, b) => a-b);
}


// TC
const numbers = [2, 1, 3, 4, 1];
console.log(solution(numbers)); // [2, 3, 4, 5, 6, 7]
