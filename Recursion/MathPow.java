package Algorithm_exercise.Recursion;

public class MathPow {
    public static long power(int base, int exponent) {
        //재귀함수
        if(exponent == 0) return 1;

        int half = exponent / 2;
        long temp = power(base, half);
        long result = (temp * temp) % 94906249;

        if(exponent % 2 == 1) return (base * result) % 94906249;
        else return result;
    }

    public static void main(String[] args) {
        long output = power(3, 40);
        System.out.println(output); // --> 19334827
    }
}
