package Algorithm_exercise.Greedy;

public class movingStuff1 {
    // 박스에 짐을 담아서, 모든 짐을 옮긴다.
    public static int movingStuff(int[] stuff, int limit) {
        // TODO:

        // 한 박스는 무게제한 limit을 넘을 수 없다.
        int[] weight = stuff;
        boolean[] use = new boolean[stuff.length];
        int box = 0;
        int boxWeight = 0;

        // 1번 짐부터 담는다.
        for (int i = 0; i < weight.length; i++){
            if (!use[i]){
                boxWeight = weight[i];
                use[i] = true;
                int max = 0;
                int maxIndex = 0;

                for (int j = 0; j < weight.length; j++) {
                    // 담고 남은 무게에 가장 가까운 짐을 담는다.
                    if ((weight[j] <= limit - boxWeight) && !use[j] && max < weight[j]){
                        max = weight[j];
                        maxIndex = j;
                    }
                }
                use[maxIndex] = true;
                box ++;
            }
        }

        return box;
    }
    public static void main(String[] args){
        int output = movingStuff(new int[]{70, 50, 80, 50}, 100);
        System.out.println(output); // 3

        output = movingStuff(new int[]{60, 80, 120, 90, 130}, 140);
        System.out.println(output); // 4

    }
}
