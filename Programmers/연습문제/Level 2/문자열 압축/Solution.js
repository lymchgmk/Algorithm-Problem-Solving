function solution(s) {
    let answer = s.length;
    for (let length=1; length<s.length/2+1; length++) {
        let slice = getSlice(s, length);
        let zippedLength = getZippedLength(slice);
        if (answer > zippedLength) {
            answer = zippedLength;
        }
    }
    return answer;
}

function getSlice(s, length) {
    let pattern = new RegExp('.{1,' + length + '}', 'g');
    return s.match(pattern);
}

function getZippedLength(slice) {
    let zipped = ''
    let lastWord = '';
    let count = NaN;
    for (const word of slice) {
        if (word != lastWord) {
            zipped += count >= 2 ? count : '';
            zipped += lastWord;
            count = 1;
        } else {
            count++;
        }
        lastWord = word;
    }
    zipped += count >= 2 ? count : '';
    zipped += lastWord;
    return zipped.length;
}


// TC
const s = "ababcdcdababcdcd";
console.log(solution(s));
