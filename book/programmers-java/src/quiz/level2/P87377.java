package quiz.level2;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;


/**
 * <a href="https://school.programmers.co.kr/learn/courses/30/lessons/87377">교점에 별 만들기</a>
 */
public class P87377 {
    private record TestCase(int[][] line, String[] answer) { }
    public static void main(String[] args) {
        TestCase[] testCases = {
                new TestCase(new int[][]{{2, -1, 4}, {-2, -1, 4}, {0, -1, 1}, {5, -8, -12}, {5, 8, 12}}, new String[]{"....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"}),
                new TestCase(new int[][]{{0, 1, -1},{1, 0, -1},{1, 0, 1}}, new String[]{"*.*"}),
                new TestCase(new int[][]{{1, -1, 0},{2, -1, 0}}, new String[]{"*"}),
                new TestCase(new int[][]{{1, -1, 0},{2, -1, 0},{4, -1, 0}}, new String[]{"*"}),
        };

        IntStream.range(0, testCases.length).forEach(idx -> {
            System.out.printf("%d 정답 %c\n", idx + 1, Arrays.equals(solution(testCases[idx].line), testCases[idx].answer) ? 'o': 'x');
        });
    }

    private static class Point {
        public final long x, y;

        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
    private static class Line {
        public final int a, b, c;

        public Line(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public Line(int[] params) {
            this.a = params[0];
            this.b = params[1];
            this.c = params[2];
        }

        public Point getIntegerIntersection(Line l) {
            if (l.a * this.b == l.b * this.a) {
                return null;
            }

            double x = (double) (l.b * this.c - this.b * l.c) / (l.a * this.b - this.a * l.b);
            double y = (double) (this.a * l.c - l.a * this.c) / (l.a * this.b - this.a * l.b);

            if (x % 1 != 0 || y % 1 != 0) {
                return null;
            }

            return new Point((long) x, (long) y);
        }
    }

    public static Point getMinimumPoint(List<Point> points) {
        long minX = Long.MAX_VALUE, minY = Long.MAX_VALUE;

        for (Point point: points) {
            minX = Math.min(minX, point.x);
            minY = Math.min(minY, point.y);
        }
        return new Point(minX, minY);
    }

    public static Point getMaximumPoint(List<Point> points) {
        long maxX = Long.MIN_VALUE, maxY = Long.MIN_VALUE;

        for (Point point: points) {
            maxX = Math.max(maxX, point.x);
            maxY = Math.max(maxY, point.y);
        }
        return new Point(maxX, maxY);
    }

    public static String[] solution(int[][] _lines) {
        List<Line> lines = Arrays.stream(_lines).map(Line::new).collect(Collectors.toList());
        List<Point> intersectionPoints = new ArrayList<>();

        // x, y 좌표가 정수인 교점들 구하기
        for (int i = 0; i < lines.size(); i++) {
            for (int j = i + 1; j < lines.size(); j++) {
                Point point = lines.get(i).getIntegerIntersection(lines.get(j));

                if (point != null) {
                    intersectionPoints.add(point);
                }
            }
        }

        // 교점들의 가장 작은 x, y 값을 가진 새로운 점 구하기. 직사각형중 왼쪽 아래 좌표
        Point maxPoint = getMaximumPoint(intersectionPoints);
        // 교점들의 가장 큰 x, y 값을 가진 새로운 점 구하기. 직사각형중 오른쪽 위 좌표
        Point minPoint = getMinimumPoint(intersectionPoints);


        int width = (int) (maxPoint.x - minPoint.x + 1);
        int height = (int) (maxPoint.y - minPoint.y + 1);

        char[][] coords = new char[height][width];
        for (int y = 0; y < height; y++) {
            Arrays.fill(coords[y], '.');
        }

        for (Point point: intersectionPoints) {
            int x = (int) (point.x - minPoint.x);
            int y = (int) (maxPoint.y - point.y);

            coords[y][x] = '*';
        }

        return Arrays.stream(coords).map(String::new).toArray(String[]::new);
    }
}
