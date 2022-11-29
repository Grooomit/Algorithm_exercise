package Algorithm_exercise.Greedy;

public class Penny {
    public static void main(String[] args){
        // 4000원을 받았을 때 500원짜리 동전 8개를 반환합니다.
        int output1 = partTimeJob(4000);
        System.out.println(output1); // --> 8

        // 4972원을 받았을 때 500원짜리 동전 9개, 100원짜리 동전 4개, 50원짜리 동전 1개, 10원짜리 동전 2개, 1원짜리 동전 2개, 총 18개를 반환합니다.
        int output2 = partTimeJob(4972);
        System.out.println(output2); // --> 18
    }

    // 동전 개수를 최소화하여 거스름돈을 만들기
    public static int partTimeJob(int k) {
        // TODO:
        // 동전 금액이 큰순으로 거스름돈을 나눠서 거슬러준다.

        // 동전 금액 배열을 만든다 (내림차순)
        int[] coins = {500, 100, 50, 10, 5, 1};
        int coinNum = 0;
        int remainder = k;

        // 거스름돈을 동전금액 배열순으로 나눠서 몫을 구한다.
        for (int coin : coins) {
            // 거스름돈 - (몫*동전금액) 을 또 다음 동전금액으로 나눈다.. 반복
            coinNum += Math.floorDiv(remainder,coin);
            remainder = Math.floorMod(remainder,coin);
            // 몫의 합 = 동전 갯수
        }
        // 몫의 합을 반환한다.
        return coinNum;
    }
}
