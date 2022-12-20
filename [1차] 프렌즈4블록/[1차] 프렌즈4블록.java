import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;

        String[][] boardArray = new String[m][n];

        int tmp = 0;
        for (String row : board) {
            boardArray[tmp] = row.split("");
            ++tmp;
        }

        boolean has4block = true;

        while (has4block) {
            has4block = false;
            List<List<Integer>> fourBlock = new ArrayList<>();
            for (int row = 0; row < m - 1; row++)
                for (int col = 0; col < n - 1; col++) {
                    if (!boardArray[row][col].equals("*")) {
                        if (checkBlocks(row, col, boardArray)) {
                            has4block = true;
                            List<Integer> tmpList = new ArrayList<>();
                            tmpList.add(row);
                            tmpList.add(col);
                            fourBlock.add(tmpList);
                        }
                    }
                }

            for (List<Integer> startIdx : fourBlock) {
                int row, col;
                row = startIdx.get(0);
                col = startIdx.get(1);
                boardArray[row][col] = "*";
                boardArray[row][col + 1] = "*";
                boardArray[row + 1][col] = "*";
                boardArray[row + 1][col + 1] = "*";
            }

            for (int col = n - 1; 0 <= col; col--) {
                int blank = -1;
                for (int row = m - 1; 0 <= row; row--) {
                    if (boardArray[row][col].equals("*")) {
                        blank = row;
                        break;
                    }
                }

                for (int row = blank; 0 <= row; row--) {
                    if (!boardArray[row][col].equals("*")) {
                        boardArray[blank][col] = boardArray[row][col];
                        boardArray[row][col] = "*";
                        blank--;
                    }
                }
            }
        }
        for (String[] arr : boardArray)
            for (String block : arr)
                if (block.equals("*"))
                    answer++;

        return answer;
    }

    boolean checkBlocks(int row, int col, String[][] board) {
        for (int i=0; i<2; i++)
            for (int j=0; j<2; j++) {
                if (!board[row][col].equals(board[row+i][col+j]))
                    return false;
            }
        return true;
    }
}
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int m = 6;
        int n = 6;
        String[] board = {"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"};

        System.out.println(sol.solution(m, n, board));
    }
}
