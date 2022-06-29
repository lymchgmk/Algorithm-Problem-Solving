function solution(progresses, speeds) {
    let plan = getPlan(progresses, speeds);
    const answer = getAnswer(plan);
    return answer;
}

function getPlan(progresses, speeds) {
    return progresses.map(
        (progress, idx) => Math.ceil((100 - progress) / speeds[idx])
    );
}

function getAnswer(plan) {
    let answer = [0];
    let maxDay = plan[0];
    for (let i=0, j=0; i<plan.length; i++) {
        if (plan[i] <= maxDay) {
            answer[j]++;
        } else {
            maxDay = plan[i];
            answer[++j] = 1;
        }
    }
    return answer;
}

arr = [0];
arr[1] = 2;
console.log(arr)