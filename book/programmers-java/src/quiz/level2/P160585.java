package quiz.level2;

import java.util.Arrays;
import java.util.stream.IntStream;


/**
 * <a href="https://school.programmers.co.kr/learn/courses/30/lessons/160585">혼자서 하는 틱택토</a>
 */
public class P160585 {
    private record TestCase(String[] board, int answer) { }

    private static class Time {
        public int h;
        public int m;
        public int s;
        public int timestamp;
        public Time(int h, int m, int s) {
            this.h = h;
            this.m = m;
            this.s = s;
            this.timestamp = 3600 * h + 60 * m + s;
        }
    }
    public static void main(String[] args) {
        TestCase[] testCases = {
                new TestCase(new String[]{"O.X", ".O.", "..X"}, 1),
                new TestCase(new String[]{"OOO", "...", "XXX"}, 0),
                new TestCase(new String[]{"...", ".X.", "..."}, 0),
                new TestCase(new String[]{"...", "...", "..."}, 1),
        };

        IntStream.range(0, testCases.length).forEach(idx -> {
            System.out.printf("%d 정답 %c\n", idx + 1, solution(testCases[idx].board) == testCases[idx].answer ? 'o' : 'x');
        });
    }

    /**
     * 1. O, X 를 순서를 지키지 않고 진행했을 수 있다 -> O 의 개수 >= X 의 개수, 차이는 0 또는 1 만 가능
     * 2. 게임의 승패가 가려진 이후에도 종료하지 않고 게임을 진행했을 수 있다
     *      2-1. 승자가 파악이 되는 경우
     *          2-1-1. 선공은 O 이므로, O 가 승리했다면, O 의 수가 한개 더 많다.
     *          2-1-2. X 가 승리했다면, X 와 O 의 수가 동일하다.
     *      2-2. 승자가 누구인지 파악이 안되는경우 -> return 0
     *
     */

    private static final char O_SIGN = 'O';
    private static final char X_SIGN = 'X';
    private static final char EMPTY = '.';

    public static int solution(String[] board) {
        int oSignCount = getCountBy(board, O_SIGN);
        int xSignCount = getCountBy(board, X_SIGN);

        // 1. 순서를 지키지 않고 진행한 경우
        if (!(oSignCount - xSignCount == 1 || oSignCount == xSignCount)) {
            return 0;
        }

        // check game finish
        // [가로, 세로, 대각선]
        int[] oSignBingoCount = new int[]{0, 0, 0};
        int[] xSignBingoCount = new int[]{0, 0, 0};

        // 가로 빙고 체크
        for (String row: board) {
            if (row.indexOf(EMPTY) == -1) {
                if ((int) row.chars().filter(ch -> ch == O_SIGN).count() == 3) oSignBingoCount[0]++;
                else if ((int) row.chars().filter(ch -> ch == X_SIGN).count() == 3) xSignBingoCount[0]++;
            }
        }

        // 세로 빙고 체크
        for (int i = 0; i < 3; i++) {
            int oSignCountInVertical = 0;
            int xSignCountInVertical = 0;
            for (String row: board) {
                if (row.charAt(i) == O_SIGN) oSignCountInVertical++;
                else if (row.charAt(i) == X_SIGN) xSignCountInVertical++;
                else break;
            }

            if (oSignCountInVertical == 3) oSignBingoCount[1]++;
            else if (xSignCountInVertical == 3) xSignBingoCount[1]++;
        }

        // 하향 대각선 빙고 체크
        for (int i = 0; i < 3; i++) {
            int oSignCountInDiagonal = 0;
            int xSignCountInDiagonal = 0;

            if (board[i].charAt(i) == O_SIGN) oSignCountInDiagonal++;
            if (board[i].charAt(i) == X_SIGN) xSignCountInDiagonal++;

            if (oSignCountInDiagonal == 3) oSignBingoCount[2]++;
            else if (xSignCountInDiagonal == 3) xSignBingoCount[2]++;
        }
        // 상향 대각선 빙고 체크
        for (int i = 2; i >= 0; i--) {
            int oSignCountInDiagonal = 0;
            int xSignCountInDiagonal = 0;

            if (board[i].charAt(2 - i) == O_SIGN) oSignCountInDiagonal++;
            if (board[i].charAt(2 - i) == X_SIGN) xSignCountInDiagonal++;

            if (oSignCountInDiagonal == 3) oSignBingoCount[2]++;
            else if (xSignCountInDiagonal == 3) xSignBingoCount[2]++;
        }


        boolean isOWin = Arrays.stream(oSignBingoCount).sum() > 0;
        boolean isXWin = Arrays.stream(xSignBingoCount).sum() > 0;

        /* 둘다 이긴 경우
         * X 도 빙고 O 도 빙고가 한개씩 있는 경우
         * 한명이 이겼지만, 이긴이후 종료하지 않은 경우
         * 선공은 O 이므로, O 가 승리했다면, O 의 수가 한개 더 많다.
         * X 가 승리했다면, X 와 O 의 수가 동일하다.
         */
        if (isOWin && isXWin) {
            return 0;
        } else if (isOWin) {
            if (oSignCount == xSignCount + 1) return 1;
            else return 0;
        } else if (isXWin) {
            if (oSignCount == xSignCount) return 1;
            else return 0;
        }

        // 가능한 경우
        return 0;
    }

    public static int getCountBy(String[] board, char c) {
        return Arrays.stream(board)
                .mapToInt((row) -> (int) row.chars().filter(ch -> ch == c).count())
                .sum();
    }

}
