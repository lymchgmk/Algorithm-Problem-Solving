function solution(phone_number) {
    var answer = getScreened(phone_number);
    return answer;
}

function getScreened(phone_number) {
    const regex = new RegExp('\\d(?=\\d{4})', 'g')
    return phone_number.replace(regex, '*');
}