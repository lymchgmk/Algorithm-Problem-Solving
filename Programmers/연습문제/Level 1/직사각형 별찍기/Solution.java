import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        String answer = "*".repeat(b);
        for (int i=0; i<a; i++) {
            System.out.println(answer);
        }
    }
}