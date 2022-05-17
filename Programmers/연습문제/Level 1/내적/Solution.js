function solution(a, b) {
    const answer = dotProduct(a, b);
    return answer;
}

function dotProduct(arr1, arr2) {
    return arr1.reduce((acc, _, i) => acc += arr1[i] * arr2[i], 0);
}