func solution(_ arr:[Int]) -> Double {
    return getSum(arr) / getLength(arr)
}

func getSum(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0, +))
}

func getLength(_ arr:[Int]) -> Double {
    return Double(arr.count)
}
