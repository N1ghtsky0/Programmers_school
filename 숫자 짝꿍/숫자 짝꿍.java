import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        int[] countX = new int[10];
        for (String x : X.split("")) countX[Integer.parseInt(x)]++;
        
        int[] countY = new int[10];
        for (String y : Y.split("")) countY[Integer.parseInt(y)]++;
        
        int[] partners = new int[10];
        for (int i=9; i>=0; i--) {
            int step = Math.min(countX[i], countY[i]);
            answer += String.valueOf(i).repeat(step);
        }
        
        if (answer.equals("")) return "-1";
        else if (answer.substring(0, 1).equals("0")) return "0";
        else return answer;
    }
}
