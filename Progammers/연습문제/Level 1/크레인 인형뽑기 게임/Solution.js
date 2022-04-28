function solution(board, moves) {
    var machine = new Machine(board);
    let picked = machine.pickUp(0);
    picked = machine.pickUp(0);
    picked = machine.pickUp(0);
    picked = machine.pickUp(0);
    picked = machine.pickUp(0);
    return;
}

class Machine {
    constructor(board) {
        this.board = board;
        this.bucket = new Bucket();
    }

    pickUp(col) {
        let doll = NaN;
        for (let row=0; row < this.board.length; row++) {
            if (this.board[row][col]) {
                doll = this.board[row][col];
                console.log(this.board);
                this.board[row][col] = 0;
                console.log(this.board, doll);
                return doll
            }
        }
    }
}

class Bucket {
    constructor() {
        this.stack = [];
        this.lastDoll = NaN;
    }

}

const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
const moves = [1,5,3,5,1,2,1,4];
console.log(solution(board, moves));
