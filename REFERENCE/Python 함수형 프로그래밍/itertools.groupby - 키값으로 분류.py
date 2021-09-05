from itertools import groupby


test = [
    {'name': '김김김1', 'blood': 'A'},
    {'name': '김김김2', 'blood': 'B'},
    {'name': '김김김3', 'blood': 'O'},
    {'name': '김김김4', 'blood': 'B'},
    {'name': '김김김5', 'blood': 'A'},
    {'name': '김김김6', 'blood': 'A'},
    {'name': '김김김7', 'blood': 'AB'},
]

import operator

# sort를 해야 원하는 것처럼 묶어짐!
test.sort(key=operator.itemgetter('blood'))
grouped_test = groupby(test, key=operator.itemgetter('blood'))
for key, val in grouped_test:
    print(key, list(val))