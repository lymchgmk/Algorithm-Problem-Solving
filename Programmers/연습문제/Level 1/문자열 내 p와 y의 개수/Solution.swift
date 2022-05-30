func solution(_ s:String) -> Bool {
    var counter: [Character: Int] = [:]
    for char in s {
        counter[char, default: 0] += 1
    }
    return getValue(counter, "p") + getValue(counter, "P") == getValue(counter, "y") + getValue(counter, "Y")
}

func getValue(_ counter: Dictionary<Character, Int>, _ key: Character) -> Int {
    return counter[key] != nil ? counter[key]! : 0
}


// TC
let s = "oooyY"
print(solution(s))
