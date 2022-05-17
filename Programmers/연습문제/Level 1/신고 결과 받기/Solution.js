function solution(id_list, report, k) {
    const reports = setReports(report);
    const name2idx = setName2idx(id_list);
    const counts = countReports(reports);
    const banned = checkBanned(counts, k);
    let answer = setAnswer(id_list, name2idx, reports, banned);
    return answer;
}

function setReports(report) {
    return [...new Set(report)].map(e => e.split(' '));
}

function setName2idx(id_list) {
    const name2idx = new Map();
    let idx = 0;
    for (const id of id_list) {
        name2idx.set(id, idx++);
    }
    return name2idx;
}

function countReports(reports) {
    let counts = new Map();
    for (const report of reports) {
        counts.set(report[1], counts.get(report[1])+1 || 1);
    }
    return counts
}

function checkBanned(counts, k) {
    let banned = new Map();
    for (const count of counts) {
        const name = count[0];
        banned.set(name, counts.get(name) >= k);
    }
    return banned;
}

function setAnswer(id_list, name2idx, reports, banned) {
    let answer = new Array(id_list.length).fill(0);
    for (const report of reports) {
        if (banned.get(report[1])) {
            const idx = name2idx.get(report[0])
            answer[idx]++;
        }
    }
    return answer;
}


// TC
id_list = ["muzi", "frodo", "apeach", "neo"];
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
k = 2;
console.log(solution(id_list, report, k));
