package Algorithm_exercise.Math;

import java.util.ArrayList;
import java.util.Arrays;

public class Combination {
    public static void main(String[] args){
        ArrayList<String[]> output = new ArrayList<>(combinationLoop());
        for (String[] str: output){
            System.out.println(Arrays.toString(str));
        }

    }

    public static ArrayList<String[]> combinationLoop() {
        String[] lookup = new String[]{"A","B","C","D","E"};
        ArrayList<String[]> result = new ArrayList<>();

        for (int i = 0; i < lookup.length; i++) {
            for (int j = i+1; j < lookup.length; j++) {
                for (int k = j+1; k < lookup.length; k++) {
                    String[] input = new String[]{lookup[i], lookup[j], lookup[k]};
                    result.add(input);
                }
            }
        }
        return result;
    }
}
