import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day1Part2 {
    public static void main(String[] args) {
        int sum = 0;
        int k;
        ArrayList<Integer> list = new ArrayList<Integer>();
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        File file = new File("src/input");
        try {
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                try {
                    // Split and parse the line
                    int left = Integer.parseInt(line.split(" ")[0]);
                    int right = Integer.parseInt(line.split(" ")[3]);
                    System.out.println(left + " " + right);

                    // Add to list and map
                    list.add(left);
                    map.put(right, map.getOrDefault(right, 0) + 1);
                } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
                    System.err.println("Skipping invalid line: " + line);
                }
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + file.getAbsolutePath());
            return;
        }



        for (int n: list) {
            int count = map.getOrDefault(n, 0);
            sum += n * count;
            System.out.println("list(i): " + count + ". Times this number has been seen: " + list.get(count) + ". Sum: " + sum);
        }
        System.out.println(sum);
    }
}
