import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int idx = 0; idx<commands.length; idx++){
            int i = commands[idx][0]-1;
            int j = commands[idx][1]-1;
            int k = commands[idx][2]-1;
            int[] subArray = Arrays.copyOfRange(array, i, j+1);
            Arrays.sort(subArray);
            answer[idx] = subArray[k];
        }
        return answer;
    }
}