//
//  main.swift
//  APS
//
//  Created by lymchgmk on 2022/05/17.
//

import Foundation

func solution(_ n:Int64) -> Int64 {
    let reversed = String(n).sorted(by: >).reduce("") {String($0) + String($1)}
    return Int64(reversed)!
}


let n: Int64 = 118372
print(solution(n))
