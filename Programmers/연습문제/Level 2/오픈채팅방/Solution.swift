import Foundation

func solution(_ record:[String]) -> [String] {
    var message = Message()
    for _record in record {
        let command = _record.components(separatedBy: " ")
        if command[0] == "Enter" || command[0] == "Leave" {
            message.writeLog(action: command[0], id: command[1])
        }
        if command[0] == "Enter" || command[0] == "Change" {
            message.writeNick(id: command[1], nickName: command[2])
        }
    }
    return message.log2Msg()
}

struct Message {
    static let defaultMessage = ["Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."]
    var log: [[String]] = []
    var id2nick: [String: String] = [:]
    
    mutating func writeLog(action: String, id: String) {
        self.log.append([action, id])
    }
    
    mutating func writeNick(id: String, nickName: String) {
        self.id2nick[id] = nickName
    }

    func log2Msg() -> [String] {
        var result: [String] = []
        for _log in self.log {
            let (action, _id) = (_log[0], _log[1])
            result.append(id2nick[_id]! + Self.defaultMessage[action]!)
        }
        return result
    }
}


// TC
let record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record)) // ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
