function solution(n, arr1, arr2) {
    const answer = getDecodedMap(n, arr1, arr2);
    return answer;
}

function getBinaryArray(n, arr) {
    let binaryArr = new Array();
    for (const num of arr) {
        const row = Array.from(num.toString(2)).map(a => parseInt(a));
        const L = row.length;
        for (let i=0; i<n-L; i++) {
            row.unshift(0);
        }
        binaryArr.push(row);
    }
    return binaryArr;
}

function getDecodedMap(n, arr1, arr2) {
    const binaryArr1 = getBinaryArray(n, arr1);
    const binaryArr2 = getBinaryArray(n, arr2);

    let decodedMap = new Array(n);
    for (let i=0; i<n; i++) {
        decodedMap[i] = new Array(n);
    }

    for (let r=0; r<n; r++) {
        for (let c=0; c<n; c++) {
            decodedMap[r][c] = binaryArr1[r][c] || binaryArr2[r][c] ? '#' : ' ';
        }
    }

    for (let i=0; i<n; i++) {
        decodedMap[i] = decodedMap[i].join('');
    }

    return decodedMap;
}


// TC
const n = 5;
const arr1 = [9, 20, 28, 18, 11];
const arr2 = [30, 1, 21, 17, 28];
console.log(solution(n, arr1, arr2)); // ["#####","# # #", "### #", "# ##", "#####"]
