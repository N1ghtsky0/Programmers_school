import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 1;
        int[][] dxdy = new int[][]{{0, 1}, {0, -1}, {-1, 0}, {1, 0}};
        int N = maps.length;
        int M = maps[0].length;
        boolean[][] visited = new boolean[N][M];
        Queue<int[]> queue = new LinkedList<>();
        
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;
        
        while (!queue.isEmpty()) {
            answer++;
            int step = queue.size();
            for (int s=0; s<step; s++) {
                int[] state = queue.poll();
                for (int[] mv : dxdy) {
                    int nx = state[0] + mv[0];
                    int ny = state[1] + mv[1];
                    if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        if ((nx == N - 1) && (ny == M - 1))
                            return answer;
                        if (maps[nx][ny] == 1)
                            queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        return -1;
    }
}
