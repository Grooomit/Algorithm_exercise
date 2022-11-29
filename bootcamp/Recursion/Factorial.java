package Algorithm.Recursion;

import java.util.Scanner;

public class Factorial {
    public int factorial(int number){
        if (number <= 1){
            return 1;
        }
        return number * factorial(number-1);

    }

    public static void main(String[] args){

        Factorial a = new Factorial();
        Scanner scan = new Scanner(System.in);

        System.out.print("팩토리얼 할 값을 입력하세요.");
        System.out.println(a.factorial(scan.nextInt()));
    }
}
