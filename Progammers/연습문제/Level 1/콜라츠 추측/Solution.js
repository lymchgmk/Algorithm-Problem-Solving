function solution(num) {
    var answer = getCollatz(num);
    return answer;
}

function getCollatz(num) {
    let n = num;
    let count = 0;
    while (n != 1 && count < 500) {
        if (n % 2) {
            n = n*3+1;
        } else {
            n /= 2;
        }
        count++;
    }
    return count >= 500 ? -1 : count;
}