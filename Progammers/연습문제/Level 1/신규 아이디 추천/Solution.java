class Solution {
    public String solution(String new_id) {
        String step_1 = new_id.toLowerCase();
        String step_2 = step_1.replaceAll("[^a-z0-9-_.]", "");
        String step_3 = step_2.replaceAll("[.]+", ".");
        String step_4 = step_3.replaceAll("^[.]|[.]$", "");
        String step_5 = step_4;
        if (step_4.equals("")){
            step_5 = "a";
        }
        String step_6 = step_5;
        if (step_6.length() >= 16) {
            step_6 = step_6.substring(0, 15);
            step_6 = step_6.replaceAll("^[.]|[.]$", "");
        }
        String step_7 = step_6;
        if (step_6.length() <= 2) {
            while (step_7.length() < 3) {
                step_7 += step_7.charAt(step_7.length() - 1);
            }
        }
        return step_7;
    }
}