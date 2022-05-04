function solution(nums) {
    const answer = sumOfThreeIsPrime(nums);
    return answer;
}

function sumOfThreeIsPrime(arr) {
    let result = 0;
    for (let i=0; i<arr.length; i++) {
        for (let j=i+1; j<arr.length; j++) {
            for (let k=j+1; k<arr.length; k++) {
                if (isPrime(arr[i]+arr[j]+arr[k])) {
                    result++;
                }
            }
        }
    }
    return result;
}

function isPrime(number) {
    for (let div=2; div<Math.sqrt(number)+1; div++) {
        if (number % div == 0) {
            return false;
        }
    }
    return true;
}


// TC
const nums = [1, 2, 3, 4];
console.log(solution(nums)); // 1