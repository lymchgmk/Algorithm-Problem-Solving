function solution(s){
    const lower_s = getLowerCase(s);
    const counter = getCounter(lower_s);
    const answer = getAnswer(counter);
    return answer;
}

function getLowerCase(str) {
    return str.toLowerCase();
}

function getCounter(str) {
    let counter = new Map();
    for (const char of Array.from(str)) {
        counter.set(char, counter.get(char) + 1 || 1);
    }
    return counter;
}

function getAnswer(counter) {
    return counter.get('p') === counter.get('y');
}