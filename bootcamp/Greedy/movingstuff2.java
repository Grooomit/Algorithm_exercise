package Algorithm_exercise.Greedy;

import java.util.Arrays;

public class movingstuff2 {
    public static void main(String[] args){
        int output = movingStuff(new int[]{70, 50, 80, 50}, 100);
        System.out.println(output); // 3

        output = movingStuff(new int[]{60, 80, 120, 90, 130}, 140);
        System.out.println(output); // 4

    }

    public static int movingStuff(int[] stuff, int limit) {
        // TODO:
        // stuff 배열을 정렬한다.
        Arrays.sort(stuff);

        int minIndex = 0;
        int maxIndex = stuff.length - 1;
        int twoStuff = 0;

        while (minIndex < maxIndex) {
            // if 가장 작은 무게와 가장 무거운 무게가 한박스에 들어가는지 확인
            if (stuff[minIndex] + stuff[maxIndex] <= limit) {
                minIndex ++;
                maxIndex --;
                twoStuff ++;
            }
            // else 안들어간다면 가장 무거운 무게만 한박스에 넣는다.
            else {
                maxIndex --;
            }
        }
        return stuff.length - twoStuff;
    }


}
