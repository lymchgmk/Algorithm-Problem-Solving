function solution(sizes) {
    const [max_w, max_h] = getMaxLengths(sizes);
    const answer = getCardSize(max_w, max_h);
    return answer;
}

function getMaxLengths(sizes) {
    let max_w = 0;
    let max_h = 0;
    for (let [w, h] of sizes) {
        [w, h] = getSorted(w, h);
        max_w = max_w < w ? w : max_w;
        max_h = max_h < h ? h : max_h;
    }
    return [max_w, max_h];
}

function getSorted(l1, l2) {
    return [l1, l2].sort((a, b) => (a-b));
}

function getCardSize(w, h) {
    return w*h;
}


// TC
const sizes = [[60, 50], [30, 70], [60, 30], [80, 40]];
console.log(solution(sizes));
