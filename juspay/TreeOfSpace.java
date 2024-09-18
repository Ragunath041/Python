import java.util.*;

public class TreeOfSpace {
    static List<String> nodes = Arrays.asList("World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt");
    static Map<String, String> status = new HashMap<>();

    public static String lock(String name) {
        int ind = nodes.indexOf(name) + 1;
        int c1 = ind * 2;
        int c2 = ind * 2 + 1;
        if (status.get(name).equals("lock") || status.get(name).equals("fail")) {
            return "false";
        } else {
            int p = ind / 2;
            status.put(nodes.get(p - 1), "fail");
            status.put(name, "lock");
            return "true";
        }
    }

    public static String unlock(String name) {
        if (status.get(name).equals("lock")) {
            status.put(name, "unlock");
            return "true";
        } else {
            return "false";
        }
    }

    public static String upgrade(String name) {
        int ind = nodes.indexOf(name) + 1;
        int c1 = ind * 2;
        int c2 = ind * 2 + 1;
        if (c1 <= nodes.size() && c2 <= nodes.size()) {
            if (status.get(nodes.get(c1 - 1)).equals("lock") && status.get(nodes.get(c2 - 1)).equals("lock")) {
                status.put(nodes.get(c1 - 1), "unlock");
                status.put(nodes.get(c2 - 1), "unlock");
                status.put(nodes.get(ind - 1), "lock");
                return "true";
            } else {
                return "false";
            }
        } else {
            return "false";
        }
    }

    public static void precompute(List<String[]> queries) {
        for (String[] query : queries) {
            status.put(query[1], "unlock");
        }
    }

    public static String operation(String name, int code) {
        String result = "false";
        if (code == 1) {
            result = lock(name);
        } else if (code == 2) {
            result = unlock(name);
        } else if (code == 3) {
            result = upgrade(name);
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 7; // Number of nodes
        int m = 2; // Some variable (not used here)
        int apis = 5; // Number of queries
        List<String[]> queries = new ArrayList<>();
        queries.add(new String[] { "1", "China" });
        queries.add(new String[] { "1", "India" });
        queries.add(new String[] { "3", "Asia" });
        queries.add(new String[] { "2", "India" });
        queries.add(new String[] { "2", "Asia" });
        precompute(queries);
        for (String[] query : queries) {
            String name = query[1];
            int code = Integer.parseInt(query[0]);
            System.out.print(operation(name, code) + " ");
        }
    }
}
