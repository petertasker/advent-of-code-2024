import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Day2Part2 {
    // Check if every neighbour is between 1 and 3 difference
    public static boolean adjacentIsNear(ArrayList<Integer> a) {
        for (int i = 1; i < a.size(); i++) {
            if (!(Math.abs(a.get(i) - a.get(i - 1)) >= 1 && Math.abs(a.get(i) - a.get(i - 1)) <= 3 )) {
                return false;
            }
        }
        return true;
    }


    public static boolean isSortedAscending(ArrayList<Integer> a) {
        for (int i = 1; i < a.size(); i++) {
            if (a.get(i) > a.get(i - 1)) {
                return false;
            }
        }
        return true;
    }


    public static boolean isSortedDescending(ArrayList<Integer> a) {
        for (int i = 1; i < a.size(); i++) {
            if (a.get(i) < a.get(i - 1)) {
                return false;
            }
        }
        return true;
    }


    public static boolean isValid(ArrayList<Integer> a) {
        return (isSortedAscending(a) || isSortedDescending(a)) && adjacentIsNear(a);
    }


    public static void main(String[] args) {
        int total = 0;
        int currentInt;
        ArrayList<Integer> list = new ArrayList<>();

        File file = new File("src/input");
        try {
            Scanner sc = new Scanner(file);
            // Read each number into an ArrayList
            while (sc.hasNext()) {
                StringTokenizer st = new StringTokenizer(sc.nextLine());
                while (st.hasMoreTokens()) {
                    currentInt = Integer.parseInt(st.nextToken());
                    list.add(currentInt);
                    //System.out.printf(currentInt + " ");
                }
                if (isValid(list)) {
                    System.out.println("Sorted!: " + list.toString());
                    total += 1;
                } else {
                    // If not valid, check all possible permutations which satisfies
                    for (int i = 0; i < list.size(); i++) {
                        ArrayList<Integer> temp = new ArrayList<>(list);
                        temp.remove(i);
                        if (isValid(temp)) {
                            total += 1;
                            break;
                        }
                    }
                    System.out.println("Not sorted!: " + list.toString());
                }
                list.clear();
            }
            sc.close();
            System.out.println("Total: " + total);
        }
        catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}