import java.util.stream.IntStream;

/**
 * <a href="    ">    </a>
 */
public class Template {
    private record TestCase(String[] args, int answer) { }
    public static void main(String[] args) {
        TestCase[] testCases = {
                new TestCase(new String[]{}, 7),
                new TestCase(new String[]{}, -1),
        };

        IntStream.range(0, testCases.length).forEach(idx -> {
            System.out.printf("%d 정답 %c\n", idx + 1, solution(testCases[idx].args) == testCases[idx].answer ? 'o': 'x');
        });
    }

    private static int solution(String[] args) {
        return 0;
    }
}
