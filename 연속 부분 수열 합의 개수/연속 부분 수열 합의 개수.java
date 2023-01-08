import java.util.HashSet;

class Solution {
    public int solution(int[] elements) {
        HashSet<Integer> answer = new HashSet<>();
        int n = elements.length;

        int[] arr = new int[2*n+1];
        System.arraycopy(elements, 0, arr, 1, n);
        System.arraycopy(elements, 0, arr, n+1, n);

        for (int i=1; i<2*n+1; i++)
            arr[i] += arr[i-1];

        for (int i=1; i<=n; i++)
            for (int j=0; j<n+1; j++) {
                int tmp = arr[j+i] - arr[j];
                answer.add(tmp);
            }
        return answer.size();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.solution(new int[]{7,9,1,1,4})); // 18
    }
}
