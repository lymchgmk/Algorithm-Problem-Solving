import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map <String, Integer> hm = new HashMap<>();
        int val = 0;

        for (String pc: participant){
            if (hm.get(pc) == null){
                hm.put(pc, 1);
            } else {
                val = hm.get(pc) + 1;
                hm.put(pc, val);
            }
        }
        
        for (String cp: completion){
            val = hm.get(cp) - 1;
            hm.put(cp, val);
        }

        for (String key: hm.keySet()){
            if (hm.get(key) == 1){
                answer = key;
            }
        }

        return answer;
    }
}


class Solution_2 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);
        
        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
                break;
            }
        }
        return answer;
    }
}