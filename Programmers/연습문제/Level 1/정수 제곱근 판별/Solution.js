function solution(n) {
    const root = getRoot(n);
    const answer = getAnswer(n, root);
    return answer;
}

function getRoot(n) {
    return parseInt(Math.sqrt(n));
}

function getAnswer(n, root) {
    return root ** 2 == n ? (root + 1) ** 2 : -1;
}