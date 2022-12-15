class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        for (int target_idx = 0; target_idx < s.length(); target_idx++) {
            char target = s.charAt(target_idx);
            int result = -1;
            for (int idx = 0; idx < target_idx; idx++) {
                char c = s.charAt(idx);
                if (target == c)
                    result = target_idx - idx;
            }
            answer[target_idx] = result;
        }
        return answer;
    }
}
