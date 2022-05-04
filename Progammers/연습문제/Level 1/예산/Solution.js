function solution(d, budget) {
    var d = d.sort((a, b) => (a-b));
    while (sum(d) > budget) {
        d.pop();
    }
     const answer = getAnswer(d);
     return answer;
}

function sort(arr) {
    return arr.sort((a, b) => (a-b));
}

function sum(arr) {
    let result = 0;
    for (const num of arr) {
        result += num;
    }
    return result;
}

function getAnswer(arr) {
    return arr.length;
}


// TC
const d = [1,3,2,5,4];
const budget = 9;
console.log(solution(d, budget));
