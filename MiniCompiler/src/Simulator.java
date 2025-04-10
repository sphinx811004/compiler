import java.util.*;

public class Simulator {
    static Map<String, Integer> vars = Map.of("a", 2, "b", 3, "c", 4);
    static Map<String, Integer> temps = new HashMap<>();

    public static void run(List<String> code) {
        for (String line : code) {
            String[] p = line.split("[ ,]+");
            switch (p[0]) {
                case "LOAD" -> temps.put(p[1], vars.get(p[2]));
                case "LOADI" -> temps.put(p[1], Integer.parseInt(p[2]));
                case "MADD" -> {
                    int val = temps.get(p[2]) * temps.get(p[3]) + temps.get(p[4]);
                    temps.put(p[1], val);
                }
            }
            System.out.println(line);
        }
        System.out.println("Final result: " + temps);
    }
}