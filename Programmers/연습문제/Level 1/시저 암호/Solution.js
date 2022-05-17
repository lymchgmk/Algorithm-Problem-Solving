function solution(s, n) {
    const ceaserCodes = getCeaserCodes(s, n);
    return ceaserCodes;
}

function getCeaserCodes(s, n) {
    let ceaserCodes = '';
    const chars = [...s]
    for (const char of chars) {
        if (char == ' ') {
            ceaserCodes += ' ';
            continue;
        }

        let ceaser = char.charCodeAt(0);
        console.log(ceaser)
        if (65 <= ceaser && ceaser <= 90) {
            ceaser = (ceaser + n - 65) % 26 + 65
        } else if (97 <= ceaser && ceaser <= 122) {
            ceaser = (ceaser + n - 97) % 26 + 97
        }
        console.log(ceaser)
        ceaserCodes += String.fromCharCode(ceaser);
    }
    return ceaserCodes;
}