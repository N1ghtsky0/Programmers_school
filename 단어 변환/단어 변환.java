import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;

        if (!Arrays.asList(words).contains(target))
            return answer;

        Queue<String> queue = new LinkedList<>();
        queue.add(begin);

        HashMap<String, Boolean> map = new HashMap<>();
        for (String word : words)
            map.put(word, false);

        map.replace(begin, true);

        while (queue.size() > 0) {
            int l = queue.size();
            for (int i=0; i<l; i++) {
                begin = queue.poll();
                for (String word : words) {
                    if (!map.get(word)) {
                        int dup = 0;
                        for (int j=0; j<word.length(); j++) {
                            if (!begin.split("")[j].equals(word.split("")[j])) dup++;
                        }
                        if (dup == 1) {
                            if (word.equals(target)) return ++answer;
                            map.replace(word, true);
                            queue.add(word);
                        }
                    }
                }
            }
            answer++;
        }
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        String begin = "hit";
        String target = "cog";
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog"};

        System.out.println(sol.solution(begin, target, words));
        // 4
    }
}
