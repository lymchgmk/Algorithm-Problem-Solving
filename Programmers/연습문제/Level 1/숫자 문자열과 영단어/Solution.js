function solution(s) {
    const answer = eng2num(s);
    return answer;
}

function eng2num(str) {
    const dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    } 

    for (const eng in dict) {
        str = str.replace(new RegExp(eng, 'g'), dict[eng]);
    }

    return Number(str);
}

s = "one4seveneight";
console.log(solution(s));