func solution(_ n:Int, _ m:Int) -> [Int] {
    return getAnswer(n, m)
}

func getAnswer(_ n: Int, _ m: Int) -> [Int]{
    let GCD: Int = getGCD(n, m)
    let LCM: Int = getLCM(n, m, GCD)
    return [GCD, LCM]
}

func getGCD(_ n:Int, _ m:Int) -> Int {
    let (n, m) = (min(n, m), max(n, m))
    var (div, GCD) = (1, 1)
    while div <= n {
        if n % div == 0 && m % div == 0 {
            GCD = div
        }
        div += 1
    }
    return GCD
}

func getLCM(_ n: Int, _ m: Int, _ GCD: Int) -> Int{
    return n * m / GCD
}
