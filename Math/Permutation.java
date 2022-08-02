package Algorithm_exercise.Math;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class Permutation {
    public static ArrayList<String[]> permutation(){
        String[] lookup = new String[]{"A","B","C"};
        ArrayList<String[]> result = new ArrayList<>();

        for (int i = 0; i < lookup.length; i++) {
            for (int j = 0; j < lookup.length; j++) {
                for (int k = 0; k < lookup.length; k++) {
                    if (i == j || j == k || k == j) continue;
                    String[] input = new String[]{lookup[i], lookup[j], lookup[k]};
                    result.add(input);
                }
            }
        }
        return result;
    }
    public static void main(String[] args){
        ArrayList<String[]> output = new ArrayList<>(permutation());
        for (String[] str: output){
            System.out.println(Arrays.toString(str));
        }
    }
}
