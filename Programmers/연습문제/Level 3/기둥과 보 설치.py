def solution(n, build_frame):
    def can_build(x, y, a):
        pillar, dam = structures_dict[0], structures_dict[1]
        # 보 인경우
        if a:
            if ([x, y-1, 0] in pillar or [x+1, y-1, 0] in pillar) or ([x-1, y, 1] in dam and [x+1, y, 1] in dam):
                return True
        # 기둥 인경우
        else:
            if y == 0 or ([x-1, y, 1] in dam or [x, y, 1] in dam) or [x, y-1, 0] in pillar:
                return True
        return False
    
    structures_dict = {0: [], 1: []}
    for x, y, a, is_build in build_frame:
        # a: 0은 기둥 / 1은 보
        if is_build:
            if can_build(x, y, a):
                structures_dict[a].append([x, y, a])
        else:
            structures_dict[a].remove([x, y, a])
            for st_x, st_y, st_a in structures_dict[0] + structures_dict[1]:
                if not can_build(st_x, st_y, st_a):
                    structures_dict[a].append([x, y, a])
                    break
    
    structures = structures_dict[0] + structures_dict[1]
    return sorted(structures, key=lambda st: (st[0], st[1], st[2]))


n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))