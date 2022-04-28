function solution(lottos, win_nums) {
    const checked = checkNums(lottos, win_nums);
    const maxRank = getRanking(checked.zeros + checked.wins);
    const minRank = getRanking(checked.wins);
    return [maxRank, minRank];
}

function checkNums(lottos, win_nums) {
    let checked = {
        "zeros": 0,
        "wins": 0
    }

    let idx = 0;
    for (const lotto of lottos) {
        if (lotto == 0) {
            checked.zeros++;
        } else if (win_nums.includes(lotto)) {
            checked.wins++;
        }
    }

    return checked;
}

function getRanking(wins) {
    const ranking = {6:1, 5:2, 4:3, 3:4, 2:5};
    return ranking[wins] || 6;
}


// TC
lottos = [44, 1, 0, 0, 31, 25];
win_nums = [31, 10, 45, 1, 6, 19];
console.log(solution(lottos, win_nums));
