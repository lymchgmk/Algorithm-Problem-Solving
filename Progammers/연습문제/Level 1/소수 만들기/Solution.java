import java.util.Arrays;

class Solution {
    public int[] combinations(int[] nums, int target){
        boolean[] visited = new boolean[nums.length];
        for(int r=1; r<=nums.length; r++){
            
        }
    }
    public boolean isPrime(int target) {
        for(int div=0; div<=Math.sqrt(target)+1; div++) {
            if(target % div == 0) {
                return false;
            }
        }
        return true;
    }
    public int solution(int[] nums) {
        int answer = 0;
        for(int[] comb : Combinations(nums, 3)){
            int sum = Arrays.stream(comb).sum();
            if(isPrime(sum)){
                answer += 1;
            }
        }
        return answer;
    }
}