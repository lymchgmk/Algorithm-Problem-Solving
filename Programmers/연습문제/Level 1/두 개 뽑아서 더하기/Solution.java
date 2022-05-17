import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> sums = new ArrayList<Integer>();
        for (int i=0; i<numbers.length - 1; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                int nums = numbers[i] + numbers[j];
                if (!sums.contains(nums)) {
                    sums.add(nums);
                }
            }
        }
        int[] answer = new int[sums.size()];
        for (int i = 0; i < sums.size(); i++) {
            answer[i] = sums.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}