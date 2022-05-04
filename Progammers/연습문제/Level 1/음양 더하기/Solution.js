function solution(absolutes, signs) {
    const answer = sum(absolutes, signs);
    return answer;
}

function sum(absolutes, signs) {
    let result = 0;
    for (const idx in absolutes) {
        result += absolutes[idx] * (signs[idx] ? 1 : -1);
    }
    return result;
}


// TC
const absolutes = [4, 7, 12];
const signs = [true, false, true];
console.log(solution(absolutes, signs)); // 9