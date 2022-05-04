function solution(arr1, arr2) {
    var answer = getSum(arr1, arr2);
    return answer;
}

function getArray(r, c) {
    return Array.from(Array(r), () => new Array(c));
}

function getSum(arr1, arr2) {
    const [max_r, max_c] = [arr1.length, arr1[0].length];
    const sum = getArray(max_r, max_c);
    for (let r=0; r<max_r; r++) {
        for (let c=0; c<max_c; c++) {
            sum[r][c] = arr1[r][c] + arr2[r][c];
        }
    }
    return sum;
}