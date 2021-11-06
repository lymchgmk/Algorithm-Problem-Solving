import java.util.Arrays;

class Solution {
    public int solution(int[] nums) {
        int ans = 0;

        for(int i = 0; i < nums.length - 2; i ++){
            for(int j = i + 1; j < nums.length - 1; j ++){
                for(int k = j + 1; k < nums.length; k ++ ){
                    if(isPrime(nums[i] + nums[j] + nums[k])){
                        ans += 1;  
                    } 
                }
            }
        }
        return ans;
    }
    public boolean isPrime(int target){
        boolean flag = true;
        for(int d=2; d<=(int)Math.sqrt(target); d++){
            if(target % d == 0){
                flag = false;
                break;
            }
        }
        return flag;
    }
}