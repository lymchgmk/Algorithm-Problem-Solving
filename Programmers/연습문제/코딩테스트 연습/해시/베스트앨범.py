genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

def my_solution(genres, plays):
    answer = []
    musics = {}
    for idx, val in enumerate(zip(genres, plays)):
        if val[0] not in musics.keys():
            musics.setdefault(val[0], [val[1], [idx, val[1]]])
        else:
            temp = musics[val[0]]
            temp.append([idx, val[1]])
            temp[0] += val[1]
            musics.setdefault(val[0], temp)

    musics_sorted = sorted(musics.items(), key=lambda x: x[1][0], reverse=True)

    for music in musics_sorted:
        for m in sorted(music[1][1:], key = lambda x: x[1], reverse=True)[:2]:
            answer.append(m[0])

    return answer

def my_solution2(genres, plays):
    answer = []
    musics = {}
    for idx, val in enumerate(zip(genres, plays)):
        if val[0] not in musics.keys():
            musics.setdefault(val[0], [val[1], [idx, val[1]]])
        else:
            musics[val[0]][0] += val[1]
            musics[val[0]].append([idx, val[1]])

    musics_sorted = sorted(musics.items(), key=lambda x: x[1][0], reverse=True)

    for music in musics_sorted:
        for m in sorted(music[1][1:], key = lambda x: x[1], reverse=True)[:2]:
            answer.append(m[0])

    return answer

def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


print(my_solution2(genres, plays))