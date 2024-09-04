import java.util.*;

public class IdSubString {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            String str = in.nextLine();
            int n = str.length();
            
            // List to store all substrings
            ArrayList<String> arr = new ArrayList<>();
            
            // Generate all substrings
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j <= n; j++) {
                    String t = str.substring(i, j);
                    arr.add(t);
                }
            }
            
            // Sort substrings and print the largest one
            Collections.sort(arr);
            
            if (!arr.isEmpty()) {
                System.out.print(arr.get(arr.size() - 1));
            } else {
                System.out.print(""); // Handle the case of empty input string
            }
        }
    }
}