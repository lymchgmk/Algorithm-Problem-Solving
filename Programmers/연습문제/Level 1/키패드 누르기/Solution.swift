import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    let pad: Pad = Pad()
    var answer = ""
    for number in numbers {
        answer += pad.selectThumb(String(number), hand)
    }
    return answer
}

struct Pad {
    static let buttons = [
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2)
    ]
    
    static var leftThumb = Thumb("left"), rightThumb = Thumb("right")
    
    func getPosition(_ button: String) -> (Int, Int) {
        return Pad.buttons[button] ?? (0, 0)
    }
    
    func calcDistance(_ button1: String, _ button2: String) -> Int {
        let position1 = self.getPosition(button1)
        let position2 = self.getPosition(button2)
        return abs(position1.0 - position2.0) + abs(position1.1 - position2.1)
    }
    
    func selectThumb(_ targetButton: String, _ hand: String) -> String {
        if Self.leftThumb.only.contains(targetButton) {
            Self.leftThumb.button = targetButton
            return "L"
        }
        if Self.rightThumb.only.contains(targetButton) {
            Self.rightThumb.button = targetButton
            return "R"
        }
        
        let leftDistance = calcDistance(Self.leftThumb.button, targetButton)
        let rightDistance = calcDistance(Self.rightThumb.button, targetButton)
        if leftDistance < rightDistance {
            Self.leftThumb.button = targetButton
            return "L"
        } else if leftDistance > rightDistance {
            Self.rightThumb.button = targetButton
            return "R"
        } else {
            if (hand == "left") {
                Self.leftThumb.button = targetButton
                return "L"
            } else {
                Self.rightThumb.button = targetButton
                return "R"
            }
        }
    }
}

class Thumb {
    let hand: String
    let only: [String]
    var _button: String
    var button: String {
        get {
            return _button
        }
        
        set(newButton) {
            _button = newButton
        }
    }
    
    init(_ hand: String) {
        self.hand = hand
        self.only = hand == "left" ? ["1", "4", "7"] : ["3", "6", "9"]
        self._button = hand == "left" ? "*" : "#"
    }
}


// TC
let numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
let hand = "right"
print(solution(numbers, hand)) // "LRLLLRLLRRL"
