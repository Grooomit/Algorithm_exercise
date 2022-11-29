package Algorithm.Recursion;

import java.util.Scanner;

public class Gugudan {
    public void Gugudan(int level, int count){
        if(count > 9){
            return;
        }
        System.out.printf("%d x %d = %d\n", level, count, level*count);
        Gugudan(level, count+1);
    }

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        Gugudan a = new Gugudan();
        System.out.print("단 수를 입력하세요.");
        int level = scan.nextInt();
        System.out.print("레벨을 입력하세요.");
        int count = scan.nextInt();
        a.Gugudan(level, count);
    }
}

