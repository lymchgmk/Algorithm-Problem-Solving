function solution(n) {
    const answer = getAnswer(n);
    return answer;
}

function getAnswer(n) {
    const substr = "수박";
    return substr.repeat(n/2) + (n%2 ? "수" : "");
}