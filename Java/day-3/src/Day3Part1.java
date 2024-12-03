import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day3Part1 {

    public static int mul(int a, int b) {
        return a * b;
    }


    public static void main(String[] args) {
        int sum = 0;
        int product;
        List<String[]> matches = new ArrayList<>();
        // "mul(s,s)" s = {n, nn, nnn} n = {0,1,...,9}
        Pattern pattern = Pattern.compile("\\bmul\\((\\d{1,3}),(\\d{1,3})\\)");

        File file = new File("src/input");
        try {
            // Read file and match every case where regex fits
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                Matcher matcher = pattern.matcher(line);
                while (matcher.find()) {
                    matches.add(new String[]{matcher.group(1), matcher.group(2)});
                }

            }
            // System.out.println(text);

         }
        catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        for (String[] match : matches) {
            product = mul(Integer.parseInt(match[0]), Integer.parseInt(match[1]));
            System.out.println("Match: " + match[0] + ", " + match[1] + ", Product: " + product);
            sum += product;
        }
        System.out.println("Sum: " + sum);
    }
}