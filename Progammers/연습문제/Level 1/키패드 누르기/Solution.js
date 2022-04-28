function solution(numbers, hand) {
    const pad = new Pad();
    let answer = "";
    for (let number of numbers){
        const target = String(number);
        answer += pad.selectThumb(hand, target);
    }
    return answer;
}

class Pad {
    constructor() {
        this.buttons = {
            '1': [0, 0], '2': [0, 1], '3': [0, 2],
            '4': [1, 0], '5': [1, 1], '6': [1, 2],
            '7': [2, 0], '8': [2, 1], '9': [2, 2],
            '*': [3, 0], '0': [3, 1], '#': [3, 2]
        };
        this.leftOnly = ['1', '4', '7'];
        this.rightOnly = ['3', '6', '9'];
        this.leftThumb = new Thumb("left");
        this.rightThumb = new Thumb("right");
    }

    getDistance(button1, button2) {
        const pos1 = this.buttons[button1];
        const pos2 = this.buttons[button2];
        return Math.abs(pos1[0] - pos2[0]) + Math.abs(pos1[1] - pos2[1]);
    }

    selectThumb(hand, target) {
        if (this.leftOnly.includes(target)) {
            this.leftThumb.setPosition(target);
            return 'L';
        }
        if (this.rightOnly.includes(target)) {
            this.rightThumb.setPosition(target);
            return 'R';
        }

        const leftDistance = this.getDistance(this.leftThumb.getPosition(), target);
        const rightDistance = this.getDistance(this.rightThumb.getPosition(), target);
        if (leftDistance < rightDistance) {
            this.leftThumb.setPosition(target);
            return 'L';
        } else if (leftDistance > rightDistance) {
            this.rightThumb.setPosition(target);
            return 'R';
        }

        if (hand == "left") {
            this.leftThumb.setPosition(target);
            return 'L';
        } else {
            this.rightThumb.setPosition(target);
            return 'R';
        }
    }
}

class Thumb {
    constructor(leftOrRight) {
        this.position = (leftOrRight == "left") ? "*" : "#"
    }

    getPosition() {
        return this.position;
    }

    setPosition(pos) {
        this.position = pos;
    }
}


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
hand = "right";
console.log(solution(numbers, hand));
