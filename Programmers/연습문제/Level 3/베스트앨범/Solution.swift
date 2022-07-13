import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var playLists: [String: Playlist] = [:]
    for idx in 0..<plays.count {
        let music = Music(genre: genres[idx], idx: idx, plays: plays[idx])
        var playList: Playlist = playLists[genres[idx]] ?? Playlist()
        playList.total_plays += plays[idx]
        playList.music_list.append(music)
        playLists[genres[idx]] = playList
    }
    
    var answer: [Int] = []
    let total_play_sorted = playLists.sorted(by: { $0.value.total_plays > $1.value.total_plays })
    for playList in total_play_sorted {
        let sortedPlayList = playList.value.music_list.sorted(by: { ($0.plays, -$0.idx) > ($1.plays, -$1.idx) })
        answer.append(sortedPlayList[0].idx)
        if sortedPlayList.count >= 2 {
            answer.append(sortedPlayList[1].idx)
        }
    }
    
    return answer
}

struct Music {
    var genre: String
    var idx: Int
    var plays: Int
}

struct Playlist {
    var total_plays: Int = 0
    var music_list: [Music] = []
}


// TC
let genres = ["classic", "pop", "classic", "classic", "pop"]
let plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays)) // [4, 1, 3, 0]
