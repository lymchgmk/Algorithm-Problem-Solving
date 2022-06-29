function solution(rows, columns, queries) {
    let arr = setDefaultArr(rows, columns);
    let answer = [];
    for (const query of queries) {
        arr.execQuery(query);
        answer.push(arr.min);
    }
    return answer;
}

function setDefaultArr(rows, columns) {
    let arr = Array.from(Array(rows), () => new Array(columns));
    for (let r=0; r<rows; r++) {
        for (let c=0; c<columns; c++) {
            arr[r][c] = r + c * rows + 1;
        }
    }
    return arr;
}

function execQuerys(arr, queries) {
    const results = [];
    let minNum = Infinity;
    for (const query of queries) {
        const [r1, c1, r2, c2] = query.map(q => q-1);
        let tmp = arr[r1][c1];
        
        for (let c=c2; c1<c; c--) {
            arr[r1][c] = arr[r1][c-1];
            minNum = Math.min(minNum, arr[r1][c+1]);
        }

        for (let r=r1; r<r2; r++) {
            arr[r+1][c2] = arr[r][c2];
            minNum = Math.min(minNum, arr[r+1][c2]);
        }

        for (let r=r1; r<r2; r++) {
            arr[r+1][c2] = arr[r][c2];
            minNum = Math.min(minNum, arr[r+1][c2]);
        }

        for (let r=r1; r<r2; r++) {
            arr[r+1][c2] = arr[r][c2];
            minNum = Math.min(minNum, arr[r+1][c2]);
        }


    }
}


// TC
const rows = 6;
const columns = 6;
const queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]];
console.log(solution(rows, columns, queries));