function solution(participant, completion) {
    let c_counter = arr2counter(completion);
    const answer = findDropOut(participant, c_counter);
    return answer;
}

function arr2counter(arr) {
    let counter = new Map();
    for (const el of arr) {
        counter.set(el, counter.get(el)+1 || 1);
    }
    return counter;
}

function findDropOut(participant, c_counter) {
    for (const p of participant) {
        if (!c_counter.get(p)) {
            return p;
        } else {
            c_counter.set(p, c_counter.get(p)-1);
        }
    }
}


// TC
const participant = ["mislav", "stanko", "mislav", "ana"];
const completion = ["stanko", "ana", "mislav"];
console.log(solution(participant, completion));
