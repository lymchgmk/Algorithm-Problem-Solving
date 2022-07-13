import Foundation

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    let orderCount = getOrderCount(orders, course)
    let candOrders = orderCount.filter{ $0.value >= 2}
    return pickMaxOrders(candOrders, course)
}

func getOrderCount(_ orders: [String], _ course: [Int]) -> [String: Int] {
    func combination(_ target:[String], _ target_num: Int, _ index: Int,_ tmp:[String], _ res: inout [String: Int]) {
        if tmp.count == target_num{
            let menus = tmp.sorted().joined()
            res[menus] = res[menus] == nil ? 1 : res[menus]! + 1
            return
        }
        
        for i in index ..< target.count{
            combination(target, target_num, i+1, tmp + [target[i]], &res)
        }
    }
    
    var orderCount: [String: Int] = [:]
    for order in orders {
        for size in course {
            combination(Array(order).map{ String($0) }, size, 0, [], &orderCount)
        }
    }
    return orderCount
}

func pickMaxOrders(_ candOrders: [String: Int], _ course: [Int]) -> [String] {
    var checkMaxCount: [Int: Int] = [:]
    for (key, val) in candOrders {
        checkMaxCount[key.count] = max(checkMaxCount[key.count] ?? 0, val)
    }
    
    var maxOrders: [String] = []
    for (key, val) in candOrders {
        if val == checkMaxCount[key.count]! {
            maxOrders.append(key)
        }
    }
    return maxOrders.sorted()
}


// TC
let orders = ["XYZ", "XWY", "WXA"]
let course = [2, 3, 4]
print(solution(orders, course)) // ["WX", "XY"]
