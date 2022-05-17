def solution(n):
    def hanoi(ndisks, startPeg=1, endPeg=3):
        if ndisks:
            hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
            answer.append([startPeg, endPeg])
            hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
    
    answer = []
    hanoi(n)
    return answer
        
        
n = 2
print(solution(n))