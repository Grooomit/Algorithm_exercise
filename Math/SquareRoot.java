package Algorithm_exercise.Math;

public class SquareRoot {
    public static String SquareRoot(int num) {
        // TODO:
        double output = 1;
        double[] sqrtNum = {1, 0.1, 0.01, 0.001};
        for (int i = 1; i < sqrtNum.length; i++) {
            while (output*output < num) {
                output = output + sqrtNum[i];
            }
            if (output*output == num) {
                break;
            }
            else {
                output = output - sqrtNum[i];
            }
        }

        // int sqrtNum = // sqrtNum * sqrtNum = num;
        return String.format("%.2f", output);
    }

    public static void main(String[] args){
        String output = SquareRoot(9);
        System.out.println(output); // --> "3.00"

        output = SquareRoot(6);
        System.out.println(output); // --> "2.45"
    }
}
