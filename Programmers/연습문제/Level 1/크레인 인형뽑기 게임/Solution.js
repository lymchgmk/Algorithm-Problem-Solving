function solution(board, moves) {
    let machine = new Machine(board);
    for (const move of moves) {
        const col = move - 1;
        machine.pickUp(col);
    }

    const answer = machine.getPoint();
    return answer;
}

class Machine {
    constructor(board) {
        this.board = board;
        this.bucket = new Bucket();
        this.point = 0;
    }

    pickUp(col) {
        for (let row=0; row < this.board.length; row++) {
            if (this.board[row][col] != 0) {
                const picked = this.board[row][col];
                this.setPoint(picked);
                this.board[row][col] = 0;
                return;
            }
        }
    }

    setPoint(doll) {
        if (this.bucket.getLastDoll() == doll) {
            this.bucket.pop();
            this.point += 2;
        } else {
            this.bucket.push(doll);
        }
    }

    getPoint() {
        return this.point;
    }
}

class Bucket {
    constructor() {
        this.stack = [];
    }

    getLastDoll() {
        return this.stack[this.stack.length-1] || NaN;
    }

    push(doll) {
        this.stack.push(doll);
    }

    pop() {
        if (this.stack.length) {
            this.stack.pop();
        }
    }
}

const board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
const moves = [1,5,3,5,1,2,1,4];
console.log(solution(board, moves));
