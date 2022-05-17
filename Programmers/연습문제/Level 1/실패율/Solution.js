function solution(N, stages) {
    const counts = countStages(stages);
    const rates = getFailureRates(N, stages, counts);
    const sortedRates = sortFailureRates(rates);
    const answer = getAnswer(sortedRates);
    return answer;
}

function countStages(stages) {
    let counts = new Map();
    for (const stage of stages) {
        counts.set(stage, counts.get(stage)+1 || 1);
    }
    return counts;
}

function getFailureRates(N, stages, counts) {
    let result = new Map();
    let player = stages.length;
    for (let i=1; i<N+1; i++) {
        result.set(i, parseFloat(counts.get(i) / player) || 0);
        player = player - counts.get(i) || player;
    }
    return result;
}

function sortFailureRates(rates) {
    return Array.from(rates).sort((a, b) => b[1] - a[1]);
}

function getAnswer(sortedRates) {
    const answer = [];
    for (const [key, val] of sortedRates) {
        answer.push(key);
    }
    return answer;
}


// TC
const N = 4;
const stages = [4, 4, 4, 4, 4];
console.log(solution(N, stages));
