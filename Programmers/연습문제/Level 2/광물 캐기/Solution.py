DIA, IRON, STONE = 0, 1, 2
fatigue_matrix = ((1, 1, 1), (5, 1, 1), (25, 5, 1))


def solution(picks, minerals):
    encoded_minerals = list(map(encode_mineral, minerals))
    encoded_mineral_bundles = [encoded_minerals[i: i+5] for i in range(0, 5 * len(picks), 5)]
    fatigue_bundles = []
    for bundle in encoded_mineral_bundles:
        fatigue_bundle = calc_fatigues(bundle)

        if fatigue_bundle:
            fatigue_bundles.append(fatigue_bundle)

    fatigue_bundles.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    total_fatigue = 0
    for fatigue_bundle in fatigue_bundles:
        if not any(picks):
            break

        if picks[DIA]:
            picks[DIA] -= 1
            total_fatigue += fatigue_bundle[DIA]
            continue

        elif picks[IRON]:
            picks[IRON] -= 1
            total_fatigue += fatigue_bundle[IRON]
            continue

        elif picks[STONE]:
            picks[STONE] -= 1
            total_fatigue += fatigue_bundle[STONE]
            continue

    return total_fatigue


def encode_mineral(target):
    if target == "diamond":
        return DIA
    elif target == "iron":
        return IRON
    elif target == "stone":
        return STONE


def calc_fatigues(encoded_minerals):
    fatigues = [0, 0, 0]

    for encoded_mineral in encoded_minerals:
        fatigues[DIA] += fatigue_matrix[DIA][encoded_mineral]
        fatigues[IRON] += fatigue_matrix[IRON][encoded_mineral]
        fatigues[STONE] += fatigue_matrix[STONE][encoded_mineral]

    return fatigues if any(fatigues) else None


if __name__ == "__main__":
    picks = [0, 1, 1]
    minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
    result = 50
    answer = solution(picks, minerals)
    print(f"[{answer == result}] {answer}")