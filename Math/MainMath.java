package Algorithm_exercise.Math;

import java.util.Scanner;

public class MainMath {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // 현재 위치 (x,y)
        int x = scan.nextInt();
        int y = scan.nextInt();
        int w = scan.nextInt();
        int h = scan.nextInt();

        // (0,0) <-> (x,y) <-> (w,h) 최단거리 계산

        int x_minLength = Math.min(x, w-x);
        int y_minLength = Math.min(y, h-y);

        System.out.println(Math.min(x_minLength, y_minLength));
    }
}
