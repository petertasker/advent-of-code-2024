import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Day1Part1 {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Integer> leftList = new ArrayList<>();
        ArrayList<Integer> rightList = new ArrayList<>();
        int sum = 0;
        int ans = 0;

        // Read file line by line
        File file = new File("src/input");
        try {
            Scanner sc = new Scanner(file);
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                // File has a two-spaced gap
                leftList.add(Integer.parseInt(line.split(" ")[0]));
                rightList.add(Integer.parseInt(line.split(" ")[3]));
            }
            sc.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("File not found.");
            return;
        }


        Collections.sort(leftList);
        Collections.sort(rightList);

        // Sum the absolute difference at each index of the two arrayLists.
        for (int i = 0; i < leftList.size(); i++) {
            ans = Math.abs(leftList.get(i) - rightList.get(i));
            System.out.println("Left: " + leftList.get(i) + " Right: " + rightList.get(i) + " Difference: " + ans);
            sum += ans;
        }
        System.out.println("Final Sum: " + sum);
    }

}