function solution(seoul) {
    const answer = getAnswer(seoul);
    return answer;
}

function getAnswer(seoul) {
    const idx = seoul.indexOf("Kim");
    return "김서방은 " + idx + "에 있다";
}