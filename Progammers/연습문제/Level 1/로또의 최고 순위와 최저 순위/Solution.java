import java.util.Arrays;

class Solution {
    public static int lotto645(int matches) {
        if (matches >= 2) {
            return 7 - matches;
        } else {
            return 6;
        }
    }

    public static boolean contains(int[] arr, int key) {
        return Arrays.stream(arr).anyMatch(i -> i == key);
    }

    public int[] solution(int[] lottos, int[] win_nums) {
        int matches = 0;
        int zeros = 0;
        for (int lotto : lottos) {
            if (lotto == 0) {
                zeros += 1;
            }
            else if (contains(win_nums, lotto)) {
                matches += 1;
            }
        }
        return new int[] {lotto645(matches + zeros), lotto645(matches)};
    }
}