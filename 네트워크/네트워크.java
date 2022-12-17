import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;

        List<Integer> checked = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!checked.contains(i)) {
                DFS(i, computers, checked);
                answer += 1;
            }
        }
        return answer;
    }

    void DFS(int idx, int[][] computers, List<Integer> connected) {
        for (int i = 0; i < computers[idx].length; i++) {
            if (computers[idx][i] == 1) {
                if (!connected.contains(i)) {
                    connected.add(i);
                    DFS(i, computers, connected);
                }
            }
        }
    }
}

public class Main {
    public static void main(String[] args) {
        int n = 3;
        int[][] input = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        Solution sol = new Solution();
        System.out.println(sol.solution(n, input)); // 2
    }
}
