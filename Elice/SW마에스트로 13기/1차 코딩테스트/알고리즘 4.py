if __name__ == "__main__":
    arr = [1100, 400, 800, 1300, 600, 1000]
    MIN_CAL, MAX_CAL = 2000, 2500

    L = len(arr)
    arr.sort()
    answer = 0
    for i in range(len(arr)):
        left, right = i+1, L-1
        while left < right:
            _sum = arr[i] + arr[left] + arr[right]
            if MIN_CAL <= _sum <= MAX_CAL:
                answer += 1
                left += 1
            else:
                if _sum < MIN_CAL:
                    left += 1
                elif MAX_CAL < _sum:
                    right -= 1
    print(answer)


