function solution(n) {
    const digit = ['1', '2', '4'];
    let answer = '';
    while (n>0) {
        n -= 1;
        answer = digit[n%3] + answer;
        n = parseInt(n/3);
    }
    return answer;
}