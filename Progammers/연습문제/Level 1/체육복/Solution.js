function solution(n, lost, reserve) {
    let gymSuits = setGymSuits(n, lost, reserve);
    borrowReserve(gymSuits);
    const answer = setAnswer(gymSuits);
    return answer;
}

function setGymSuits(n, lost, reserve) {
    let gymSuits = new Array(n).fill(1);
    for (const i of lost) {
        gymSuits[i-1]--;
    }
    for (const i of reserve) {
        gymSuits[i-1]++;
    }
    return gymSuits;
}

function borrowReserve(gymSuits) {
    for (let i=0; i<gymSuits.length; i++) {
        if (gymSuits[i] == 2) {
            if (i != 0 && gymSuits[i-1] == 0) {
                gymSuits[i]--;
                gymSuits[i-1]++;
            } else if (i != gymSuits.length - 1 && gymSuits[i+1] == 0) {
                gymSuits[i]--;
                gymSuits[i+1]++;
            }
        }
    }
}

function setAnswer(gymSuits) {
    return gymSuits.filter(a => a>=1).length;
}


// TC
const n = 4;
const lost = [3, 1]; 
const reserve = [2, 4];
console.log(solution(n, lost, reserve)); // 5
