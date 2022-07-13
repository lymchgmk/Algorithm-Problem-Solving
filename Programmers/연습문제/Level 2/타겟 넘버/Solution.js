function solution(numbers, target) {
    let answer = 0;
    getAnswer(0, 0);
    return answer;

    function getAnswer(idx, sum) {
        if (idx === numbers.length) {
            if (sum === target) {
                answer++;
            }
            return;
        }
        getAnswer(idx+1, sum + numbers[idx]);
        getAnswer(idx+1, sum - numbers[idx]);
    }
}