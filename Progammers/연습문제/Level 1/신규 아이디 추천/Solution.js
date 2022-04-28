function solution(new_id) {
    let id = step1(new_id);;
    id = step2(id);
    id = step3(id);
    id = step4(id);
    id = step5(id);
    id = step6(id);
    id = step7(id);
    return id;
}

function step1(str) {
    return str.toLowerCase();
}

function step2(str) {
    const regex = new RegExp('[^a-z0-9-_.]', 'g');
    const result = str.replace(regex, '');
    return result;
}

function step3(str) {
    const regex = new RegExp('[.]{2,}', 'g');
    const result = str.replace(regex, '.');
    return result
}

function step4(str) {
    const regex = new RegExp('^\\.|\\.$');
    result = str.replace(regex, '');
    return result;
}

function step5(str) {
    return str || 'a';
}

function step6(str) {
    let result = str.substr(0, 15);

    const regex = new RegExp('\\.$');
    result = result.replace(regex, '');
    return result;
}

function step7(str) {
    str = str.padEnd(3, str[str.length-1]);
    return str;
}

// TC
new_id = "...!@BaT#*..y.abcdefghijklm";
console.log(solution(new_id));
