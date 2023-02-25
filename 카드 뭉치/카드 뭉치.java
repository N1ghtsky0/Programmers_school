import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Queue<String> queue1 = new LinkedList<>();
        Queue<String> queue2 = new LinkedList<>();

        for (String word : cards1) queue1.offer(word);
        for (String word : cards2) queue2.offer(word);

        int idx;
        for (idx=0; idx<goal.length; idx++) {
            String target = goal[idx];
            if (target.equals(queue1.peek())) {
                queue1.poll();
            } else if (target.equals(queue2.peek())) {
                queue2.poll();
            } else {
                return "No";
            }
        }
        return "Yes";
    }
}
