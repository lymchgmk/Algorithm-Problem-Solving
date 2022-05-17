function solution(n) {
    var answer = countPrimeNumbers(n);
    return answer;
}

function countPrimeNumbers(n) {
    let count = 0;
    for (let num=2; num<=n; num++) {
        if (isPrimeNumber(num)) {
            count++;
        }
    }
    return count;
}

function isPrimeNumber(num) {
    for (let div=2; div<=Math.sqrt(num); div++) {
        if (num % div === 0) {
            return false;
        }
    }
    return true;
}
