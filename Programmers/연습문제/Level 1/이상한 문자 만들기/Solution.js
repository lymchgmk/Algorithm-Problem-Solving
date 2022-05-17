function solution(s) {
    const strangeWords = makeStrangeWords(splitStr(s));
    const answer = getAnswer(strangeWords);
    return answer;
}

function splitStr(s) {
    return s.split(' ');
}

function makeStrangeWords(arr) {
    let strangeWords = [];
    for (const word of arr) {
        let strangeWord = [...word];
        for (let i=0; i<strangeWord.length; i++) {
            if (i % 2) {
                strangeWord[i] = strangeWord[i].toLowerCase();
            } else {
                strangeWord[i] = strangeWord[i].toUpperCase();
            }
        }
        strangeWords.push(strangeWord.join(''));
    }
    return strangeWords;
}

function getAnswer(arr) {
    let answer = arr.join(' ');
    return answer;
}