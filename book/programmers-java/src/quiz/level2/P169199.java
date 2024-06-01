package quiz.level2;

import java.util.Queue;
import java.util.LinkedList;
import java.util.stream.IntStream;

/**
 * <a href="https://school.programmers.co.kr/learn/courses/30/lessons/169199">리코쳇 로봇</a>
 */
public class P169199 {
    private record TestCase(String[] board, int answer) { }

    private static final int[] dx = new int[]{-1, 1, 0, 0};
    private static final int[] dy = new int[]{0, 0, -1, 1};
    private static final String dKor = "상하좌우";

    public static void main(String[] args) {
        TestCase[] testCases = {
                new TestCase(new String[]{"...D..R", ".D.G...", "....D.D", "D....D.", "..D...."}, 7),
                new TestCase(new String[]{".D.R", "....", ".G..", "...D"}, -1),
        };

        IntStream.range(0, testCases.length).forEach(idx -> {
            System.out.printf("%d 정답 %c\n", idx + 1, solution(testCases[idx].board) == testCases[idx].answer ? 'o': 'x');
        });
    }

    private static int solution(String[] board) {
        int minimumMovement = -1;

        int width = board[0].length();
        int height = board.length;

        int sx = -1, sy = -1;
        int gx = -1, gy = -1;


        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length(); j++) {
                if (board[i].charAt(j) == 'R') {
                    sx = i;
                    sy = j;
                }

                if (board[i].charAt(j) == 'G') {
                    gx = i;
                    gy = j;
                }
            }
        }

        // check impossible
        boolean isNoSolution = true;
        if (gx == 0 || gx == height - 1 || gy == 0 || gy == width - 1) {
            // 가장 바깥인 경우
            isNoSolution = false;
        } else {
            // 맵을 벗어나는 경우는 존재하지 않음
            for (int i = 0; i < 4; i++) {
                int nx = gx + dx[i];
                int ny = gy + dy[i];

                if (board[nx].charAt(ny) == 'D') {
                    isNoSolution = false;
                    break;
                }
            }
        }

        if (isNoSolution) {
            return -1;
        }

        minimumMovement = bfs(board, sx, sy);

        return minimumMovement;
    }

    private static int bfs(String[] board, int sx, int sy) {
        int minimumMovement = -1;

        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{sx, sy, 0});

        int width = board[0].length();
        int height = board.length;

        boolean[][] visited = new boolean[height][width];
        visited[sx][sy] = true;

        while (!queue.isEmpty()) {
            Integer[] top = queue.poll();
            int cx = top[0];
            int cy = top[1];
            int move = top[2];

            for (int d = 0; d < 4; d++) {

                int nx = cx;
                int ny = cy;
                while (true) {
                    nx += dx[d];
                    ny += dy[d];

                    if (nx < 0 || nx == height || ny < 0 || ny == width
                            || board[nx].charAt(ny) == 'D') {
                        nx -= dx[d];
                        ny -= dy[d];
                        break;
                    }
                }

                if (visited[nx][ny]) {
                    continue;
                }

                if (board[nx].charAt(ny) == 'G') {
                    minimumMovement = move + 1;
                    queue.clear();
                    break;
                } else {
                    queue.add(new Integer[]{nx, ny, move + 1});
                    visited[nx][ny] = true;
                }
            }
        }

        return minimumMovement;
    }


}
