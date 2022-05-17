function solution(price, money, count) {
    const totalPrice = getTotalPrice(price, count);
    const answer = getLackOfMoney(totalPrice, money);
    return answer;
}

function getTotalPrice(price, count) {
    let totalPrice = price * ((count * (count + 1))/2);
    return totalPrice;
}

function getLackOfMoney(totalPrice, money) {
    return money > totalPrice ? 0 : totalPrice - money;
}


// TC
const price = 3;
const money = 20;
const count = 4;
console.log(solution(price, money, count)); // 10
