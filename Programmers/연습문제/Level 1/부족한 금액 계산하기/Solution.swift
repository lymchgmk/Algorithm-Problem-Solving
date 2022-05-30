import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    let totalCost = calcTotalCost(price, count)
    return money >= totalCost ? 0 : Int64(totalCost - money)
}

func calcTotalCost(_ price: Int, _ count: Int) -> Int {
    return price * (count * (count+1)/2)
}

    
// TC
let price = 3
let money = 20
let count = 4
print(solution(price, money, count))
