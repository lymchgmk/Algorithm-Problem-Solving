function solution(dartResult) {
    const darts = splitDarts(dartResult);
    const elements = getElements(darts);
    const points = getPoints(elements);
    const answer = getAnswer(points);
    return answer;
}

function splitDarts(dartResult) {
    const regex = new RegExp('([0-9]+[SDT][#*]?)', 'g');
    const darts = dartResult.match(regex);
    return darts;
}

function getElements(darts) {
    let elements = [];
    const regex = new RegExp('(?<num>[0-9]+)(?<SDT>[SDT])(?<opt>[#*]?)');
    for (const dart of darts) {
        elements.push(dart.match(regex).groups);
    }
    return elements;
}

function getSDT(char) {
    const SDT = {
        'S': 1,
        'D': 2,
        'T': 3
    };
    return SDT[char];
}

function getPoints(elements) {
    let points = new Array(elements.length).fill(0);
    for (let i=0; i<elements.length; i++) {
        points[i] += elements[i]['num'] ** getSDT(elements[i]['SDT']);
    }
    for (let i=0; i<elements.length; i++) {
        if (elements[i]['opt'] == '*') {
            points[i-1] *= 2;
            points[i] *= 2;
        } else if (elements[i]['opt'] == '#') {
            points[i] *= -1;
        }
    }
    return points;
}

function getAnswer(points) {
    return points.reduce((a, b) => (a+b));
}


// TC
const dartResult = "1D2S#10S";
console.log(solution(dartResult)); // 37
