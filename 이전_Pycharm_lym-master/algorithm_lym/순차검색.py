#1. 정렬 안 된 경우
def sequentialsearch1(a, n, key):
    i = 0
    while i<n and a[i] != key:
        i += 1
    if i<n : return i
    else: return -1

data = [4, 9, 11, 23, 2, 19, 7]
key = 19
print(sequentialsearch1(data, len(data), key))
print(data[sequentialsearch1(data, len(data), key)])

#2. 정렬 된 경우

def sequentialsearch2(a, n, key):
    i = 0
    i += 1
    while i<n and a[i]<key:
        i += 1
    if i<n and a[i] == key : return i
    else : return -1


