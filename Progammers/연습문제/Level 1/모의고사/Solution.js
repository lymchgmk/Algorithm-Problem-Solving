function solution(answers) {
    const patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ];

    const points = getPoints(answers, patterns);
    const answer = getAnswer(points);
    return answer;
}

function getPoints(answers, patterns) {
    let points = [];
    for (const pattern of patterns) {
        let point = 0;
        for (let i=0; i<answers.length; i++) {
            if (answers[i] == pattern[i % pattern.length]) {
                point++;
            }
        }
        points.push(point);
    }
    return points;
}

function getMaxPoint(points) {
    return Math.max(...points);
}

function getAnswer(points) {
    let answer = [];
    const maxPoint = getMaxPoint(points);
    for (let i=0; i<points.length; i++) {
        if (points[i] == maxPoint) {
            answer.push(i+1);
        }
    }
    return answer;
}


// TC
const answers = [1,3,2,4,2];
console.log(solution(answers)); // [1]
