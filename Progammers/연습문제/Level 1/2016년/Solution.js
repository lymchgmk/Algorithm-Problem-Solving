function solution(a, b) {
    const date = getDate(a, b);
    const dayOfWeek = getDayOfWeek(date);
    const answer = getAnswer(dayOfWeek);
    return answer;
}

function getDate(month, day) {
    return new Date(2016, month-1, day);
}

function getDayOfWeek(date){
    const options = {weekday: 'short'};
    return new Intl.DateTimeFormat('en-US', options).format(date);
}

function getAnswer(dayOfWeek) {
    return dayOfWeek.toString().toUpperCase();
}


// TC
const a = 5;
const b = 24
console.log(solution(a, b)); // TUE
