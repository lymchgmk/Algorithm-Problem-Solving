function solution(n, m) {
    const GCD = getGCD(n, m);
    const LCM = getLCM(n, m, GCD);
    var answer = getAnswer(GCD, LCM);
    return answer;
}

function getGCD(n, m) {
    let GCD = -Infinity;
    const [minNum, maxNum] = [n, m].sort((a, b) => a-b);
    for (let div=1; div<=minNum; div++) {
        if (minNum % div == 0 && maxNum % div == 0) {
            GCD = div;
        }
    }
    return GCD;
}

function getLCM(n, m, GCD) {
    return n * m / GCD;
}

function getAnswer(GCD, LCM) {
    return [GCD, LCM];
}