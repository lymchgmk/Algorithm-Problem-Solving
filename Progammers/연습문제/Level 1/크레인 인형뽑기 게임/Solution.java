import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> bucket = new Stack<>();
        for (int move : moves) {
            move -= 1;
            for (int depth = 0; depth < board.length; depth++) {
                int doll = board[depth][move];
                if (doll != 0) {
                    board[depth][move] = 0;
                    if (!bucket.isEmpty() && bucket.peek() == doll) {
                        bucket.pop();
                        answer += 2;
                    } else {
                        bucket.push(doll);
                    }
                    break;
                }
            }
        }
        return answer;
    }
}