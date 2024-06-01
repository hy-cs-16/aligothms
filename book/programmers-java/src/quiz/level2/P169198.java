package quiz.level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

/**
 * <a href="https://school.programmers.co.kr/learn/courses/30/lessons/169198">당구 연습</a>
 */
public class P169198 {
    private record TestCase(int m, int n, int startX, int startY, int[][] balls, int[] answer) {
    }

    public static void main(String[] args) {
        TestCase[] testCases = {
                new TestCase(10, 10, 3, 7, new int[][]{{7, 7}, {2, 7}, {7, 3}}, new int[]{52, 37, 116}),
        };

        IntStream.range(0, testCases.length).forEach(idx -> {
            System.out.printf("%d 정답 %c\n", idx + 1, Arrays.equals(solution(testCases[idx]), testCases[idx].answer) ? 'o' : 'x');
        });
    }

    private static int[] solution(TestCase t) {
        return solution(t.m, t.n, t.startX, t.startY, t.balls);
    }

    private static int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        return Arrays.stream(balls).mapToInt((ball) -> {
            int ballX = ball[0];
            int ballY = ball[1];

            List<Integer> distanceSquares = new ArrayList<>();
            // 4 방향 대칭
            // 축 x = 0
            int candidateByX_0 = (int) Math.pow((startX + ballX), 2) + (int) Math.pow((startY - ballY), 2);
            // 축 y = 0
            int candidateByY_0 = (int) Math.pow((startX - ballX), 2) + (int) Math.pow((startY + ballY), 2);
            // 축 y = n
            int candidateByY_N = (int) Math.pow((startX - ballX), 2) + (int) Math.pow((2 * n - startY - ballY), 2);
            // 축 x = m
            int candidateByX_M = (int) Math.pow((2 * m - startX - ballX), 2) + (int) Math.pow((startY - ballY), 2);

            if (startY == ballY) {
                // 축 x = 0
                if (startX < ballX) {
                    distanceSquares.add(candidateByX_0);
                    distanceSquares.add(candidateByY_0);
                    distanceSquares.add(candidateByY_N);
                    // distanceSquares.add(candidateByX_M);
                } else {
                    // distanceSquares.add(candidateByX_0);
                    distanceSquares.add(candidateByY_0);
                    distanceSquares.add(candidateByY_N);
                    distanceSquares.add(candidateByX_M);
                }
            } else if (startX == ballX) { // startY != ballY
                if (startY < ballY) {
                    distanceSquares.add(candidateByX_0);
                    distanceSquares.add(candidateByY_0);
                    // distanceSquares.add(candidateByY_N);
                    distanceSquares.add(candidateByX_M);
                } else {
                    distanceSquares.add(candidateByX_0);
                    // distanceSquares.add(candidateByY_0);
                    distanceSquares.add(candidateByY_N);
                    distanceSquares.add(candidateByX_M);
                }
            } else {
                // startX != ballX and startY != ballY
                distanceSquares.add(candidateByX_0);
                distanceSquares.add(candidateByY_0);
                distanceSquares.add(candidateByY_N);
                distanceSquares.add(candidateByX_M);
            }

            return distanceSquares.stream().min(Integer::compareTo).get();
        }).toArray();
    }

}