function solution(num) {
    var answer = getAnswer(num);
    return answer;
}

function getAnswer(num) {
    return num % 2 ? "Odd" : "Even";
}