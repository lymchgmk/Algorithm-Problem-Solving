import Foundation

func solution(_ beginning:[[Int]], _ target:[[Int]]) -> Int {
    let (rMax, cMax) = (beginning.count, beginning[0].count)

    let table = zip(beginning, target).map { (bRow, tRow) in
        zip(bRow, tRow).map { $0.0 ^ $0.1 }
    }
    let defaultRow = table[0]
    var (flipRowCount, flipColCount) = (0, defaultRow.reduce(0, +))
    for row in table {

        if row == defaultRow {
            continue
        }

        flipRowCount += 1

        if row.map({ $0 ^ 1 }) != defaultRow {
            return -1
        }
    }

    return min(flipRowCount + flipColCount, (rMax - flipRowCount) + (cMax - flipColCount))
}
