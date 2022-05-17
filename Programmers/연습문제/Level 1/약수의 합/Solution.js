function solution(n) {
    var answer = getDivSum(n);
    return answer;
}

function getDivSum(n) {
    let sum = 0;
    for (let div=1; div<=n; div++) {
        if (n % div === 0) {
            sum += div;
        }
    }
    return sum;
}