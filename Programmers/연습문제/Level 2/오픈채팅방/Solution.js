function solution(record) {
    const idDict = setIdDict(record);
    const result = getResult(record, idDict);
    return result;
}

function setIdDict(record) {
    let idDict = new Map();
    for (const rec of record) {
        const [action, id, name] = rec.split(' ');
        if (action == 'Enter' || action == 'Change') {
            idDict.set(id, name);
        }
    }
    return idDict;
}

function getResult(record, idDict) {
    let result = [];
    for (const rec of record) {
        const [action, id, name] = rec.split(' ');
        if (action == 'Enter' || action == 'Leave') {
            const message = getMessage(idDict.get(id), action);
            result.push(message);
        }
    }
    return result;
}

function getMessage(name, action) {
    const message = {
        'Enter': "님이 들어왔습니다.",
        'Leave': "님이 나갔습니다."
    }
    return name + message[action];
}