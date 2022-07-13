function solution(w, h) {
    var answer = getAnswer(w, h);
    return answer;
}

function getGCD(n1, n2) {
    let GCD = NaN;
    const [min, max] = [n1, n2].sort((a, b) => a-b);
    for (let div=1; div<=n1; div++) {
        if (min%div==0 && max%div==0) {
            GCD = div;
        }
    }
    return GCD;
}

function getAnswer(w, h) {
    const GCD = getGCD(w, h);
    return w*h - (w+h-GCD);
}