function solution(s) {
    const answer = getAnswer(s);
    return answer;
}

function getAnswer(s) {
    const arr = s.split('');
    if (arr.length % 2) {
        return 0;
    } else {
        const result = getRemoved(arr);
        return result.length ? 0 : 1;
    }
}

function getRemoved(arr) {
    let stack = [];
    for (const char of arr) {
        if (stack.length === 0) {
            stack.push(char);
        } else if (stack[stack.length-1] === char) {
            stack.pop();
        } else {
            stack.push(char);
        }
    }
    return stack;
}


// TC
const s = 'baabaa';
console.log(solution(s));