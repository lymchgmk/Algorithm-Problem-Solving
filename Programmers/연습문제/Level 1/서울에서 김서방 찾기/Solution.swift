func solution(_ seoul:[String]) -> String {
    return "김서방은 \(findKim(seoul))에 있다"
}

func findKim(_ seoul: [String]) -> String {
    return String(seoul.firstIndex(of: "Kim")!)
}


// TC
let seoul = ["Jane", "Kim"]
print(solution(seoul))
