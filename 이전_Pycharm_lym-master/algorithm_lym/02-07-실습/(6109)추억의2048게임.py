import sys
sys.stdin = open("(6109)추억의2048게임_input.txt")  # 파일에서 입력받는 경우 사용
T = int(input())
for test_case in range(1, T + 1):
    N, dir = input().split()
    N = int(N)

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    if dir == 'up':
        for col in range(N):
            stack = []
            tmp = [0] * N
            i = j = 0  # arr, tmp의 인덱스
            while i < N:
                if arr[i][col] != 0:        # 빈칸이 아니면
                    if len(stack) == 0:     # stack empty이면
                        stack.append(arr[i][col])       # stack push
                    else:
                        if stack[-1] == arr[i][col]:  # stack peek , arr비교해서 같으면
                            tmp[j] = stack.pop() * 2  # stack pop 해서 2곱해서 tmp에 저장
                            j += 1
                        else:
                            tmp[j] = stack.pop()      # stack pop해서 tmp에 저장
                            j += 1
                            stack.append(arr[i][col]) #arr값을 stack push
                i += 1
            if len(stack): tmp[j] = stack.pop()      #stack not empty일때 나머지 모두 tmp에 추가
            for i in range(N):  # tmp를 arr에 복사
                arr[i][col] = tmp[i]

    elif dir == 'down':
        for col in range(N):
            i = j = N - 1
            stack = []
            tmp = [0] * N
            while i >= 0:
                if arr[i][col] != 0:
                    if len(stack) == 0:
                        stack.append(arr[i][col])
                    else:
                        if stack[-1] == arr[i][col]:
                            tmp[j] = arr[i][col] * 2
                            j -= 1
                            stack.pop()
                        else:
                            tmp[j] = stack.pop()
                            j -= 1
                            stack.append(arr[i][col])
                i -= 1
            if len(stack): tmp[j] = stack.pop()
            for i in range(N):
                arr[i][col] = tmp[i]

    elif dir == 'left':
        for row in range(N):
            i = j = 0
            stack = []
            tmp = [0] * N
            while i < N:
                if arr[row][i] != 0:
                    if len(stack) == 0:
                        stack.append(arr[row][i])
                    else:
                        if stack[-1] == arr[row][i]:
                            tmp[j] = arr[row][i] * 2
                            j += 1
                            stack.pop()
                        else:
                            tmp[j] = stack.pop()
                            j += 1
                            stack.append(arr[row][i])
                i += 1
            if len(stack): tmp[j] = stack.pop()
            for i in range(N):
                arr[row][i] = tmp[i]

    elif dir == 'right':
        for row in range(N):
            i = j = N - 1
            stack = []
            tmp = [0] * N
            while i >= 0:
                if arr[row][i] != 0:
                    if len(stack) == 0:
                        stack.append(arr[row][i])
                    else:
                        if stack[-1] == arr[row][i]:
                            tmp[j] = arr[row][i] * 2
                            j -= 1
                            stack.pop()
                        else:
                            tmp[j] = stack.pop()
                            j -= 1
                            stack.append(arr[row][i])
                i -= 1
            if len(stack): tmp[j] = stack.pop()
            for i in range(N):
                arr[row][i] = tmp[i]

    print('#%d' % test_case)
    for i in range(N):
        for j in range(N):
            print('%d ' % arr[i][j], end="")
        print()
