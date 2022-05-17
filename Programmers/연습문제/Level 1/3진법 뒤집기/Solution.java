class Solution {
    public int solution(int n) {
        String res = "";
        while (n>0) {
            res += Integer.toString(n%3);
            n /= 3;
        }
        return Integer.parseInt(res, 3);
    }
}