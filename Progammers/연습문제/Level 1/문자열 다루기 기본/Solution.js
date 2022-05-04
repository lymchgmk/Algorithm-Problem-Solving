function solution(s) {
    const answer = getAnswer(s);
    return answer;
}

function getAnswer(s) {
    const regex = new RegExp('^\\d{4}$|^\\d{6}$');
    return regex.test(s);
}