class Solution {
    public String solution(int n) {
        int q = n / 2;
        int r = n % 2;
        return new String("수박".repeat(q) + "수박".substring(0, r));
    }
}