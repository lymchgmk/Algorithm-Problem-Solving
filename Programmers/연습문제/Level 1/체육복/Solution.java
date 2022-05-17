import java.util.Arrays;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] before = new int[n+1];
        int[] after = new int[n+1];
        Arrays.fill(before, 1);
        for (int l : lost) {
            before[l] -= 1;
        }
        for (int r : reserve) {
            before[r] += 1;
        }
        
        for (int i=1; i < n+1; i++) {
            int cnt = before[i];
            if (cnt == 0) {
                continue;
            } else if (cnt == 1) {
                after[i] = 1;
            } else {
                after[i] = 1;
                if (i != 1 && after[i-1] == 0) {
                    after[i-1] = 1;
                } else if (i != n && after[i+1] == 0) {
                    after[i+1] = 1;
                }
            }
        }

        int answer = 0;
        for (int res : after) {
            if (res == 1){
                answer++;
            }
        }
        return answer;
    }
}