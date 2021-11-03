class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr1[0].length];
        for (int i = 0; i < arr1.length; i++){
            for (int j = 0; j < arr1[0].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        return answer;
    }

    public static void main(String[] args){
        int[][] arr1 = {{1, 2}, {2, 4}};
        int[][] arr2 = {{1, 2}, {2, 4}};

        int[][] answer = new Solution().solution(arr1, arr2);
        System.out.println(answer);
    }
}