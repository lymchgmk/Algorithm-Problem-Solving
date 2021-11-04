import java.util.*;

class Solution {
    public static boolean contains(String[] arr, String key) {
        return Arrays.asList(arr).contains(key);
    }
    public static int thumbDist(HashMap<String, int[]> keyboard, String thumb, String target) {
        int[] thumbRowCol = keyboard.get(thumb);
        int[] targetRowCol = keyboard.get(target);
        return Math.abs(thumbRowCol[0] - targetRowCol[0]) + Math.abs(thumbRowCol[1] - targetRowCol[1]);
    }
    public String solution(int[] numbers, String hand) {
        String answer = "";
        HashMap<String, int[]> keyboard = new HashMap<>();
        for (int r=0; r<3; r++) {
            keyboard.put(Integer.toString(3*r+1), new int[] {r, 0});
            keyboard.put(Integer.toString(3*r+2), new int[] {r, 1});
            keyboard.put(Integer.toString(3*r+3), new int[] {r, 2});
        }
        keyboard.put("*", new int[] {3, 0});
        keyboard.put("0", new int[] {3, 1});
        keyboard.put("#", new int[] {3, 2});
        String leftThumb = "*";
        String rightThumb = "#";
        String[] onlyLeftThumb = {"1", "4", "7"};
        String[] onlyRightThumb = {"3", "6", "9"};

        for(int target : numbers) {
            String tg = Integer.toString(target);
            if (contains(onlyLeftThumb, tg)) {
                answer += "L";
                leftThumb = tg;
            } else if (contains(onlyRightThumb, tg)) {
                answer += "R";
                rightThumb = tg;
            } else {
                int leftThumbDist = thumbDist(keyboard, leftThumb, tg);
                int rightThumbDist = thumbDist(keyboard, rightThumb, tg);
                if (leftThumbDist < rightThumbDist) {
                    answer += "L";
                    leftThumb = tg;
                } else if (leftThumbDist > rightThumbDist) {
                    answer += "R";
                    rightThumb = tg;
                } else {
                    if (hand.equals("left")) {
                        answer += "L";
                        leftThumb = tg;
                    } else {
                        answer += "R";
                        rightThumb = tg;
                    }
                }
            }
        }
        return answer;
    }
}