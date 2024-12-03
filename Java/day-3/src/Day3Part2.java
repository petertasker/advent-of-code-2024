import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.MatchResult;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3Part2 {

    public static void main(String[] args) {
        int total = 0;
        int currentDoIndex = 0;
        int currentDontIndex = 0;

        try {
            // Read the input file into a single string
            File file = new File("src/input");
            String text = new String(Files.readAllBytes(file.toPath()));

            Pattern mulPattern = Pattern.compile("\\bmul\\((\\d{1,3}),(\\d{1,3})\\)");
            Matcher mulMatcher = mulPattern.matcher(text);
            List<MatchResult> mulMatches = new ArrayList<>();
            while (mulMatcher.find()) {
                mulMatches.add(mulMatcher.toMatchResult());
            }

            // Find indices of "do()" and "don't()"
            List<Integer> doIndices = findIndices(text, "\\bdo\\(\\)");
            List<Integer> dontIndices = findIndices(text, "\\bdon't\\(\\)");

            for (MatchResult match : mulMatches) {
                // Extract numbers and calculate their product
                int a = Integer.parseInt(match.group(1));
                int b = Integer.parseInt(match.group(2));
                int product = a * b;

                // Find the index of the current match in  the text
                int matchIndex = match.start();
                System.out.printf("match = (%d,%d), index = %d, product = %d%n", a, b, matchIndex, product);

                // Update currentDoIndex and currentDontIndex
                while (!doIndices.isEmpty() && doIndices.get(0) < matchIndex) {
                    currentDoIndex = doIndices.remove(0);
                }

                while (!dontIndices.isEmpty() && dontIndices.get(0) < matchIndex) {
                    currentDontIndex = dontIndices.remove(0);
                }

                System.out.printf("currentDoIndex = %d, currentDontIndex = %d%n", currentDoIndex, currentDontIndex);

                // Add product to total if "do()" is more recent than "don't()"
                if (currentDoIndex >= currentDontIndex) {
                    total += product;
                }
            }
            System.out.println(total);


        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    // Helper method to find indices of a pattern in the text
    private static List<Integer> findIndices(String text, String pattern) {
        List<Integer> indices = new ArrayList<>();
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(text);
        while (m.find()) {
            indices.add(m.start());
        }
        return indices;
    }
}