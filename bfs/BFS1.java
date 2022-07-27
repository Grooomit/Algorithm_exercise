package Algorithm_exercise.BFS;

import java.util.LinkedList;
import java.util.Queue;

public class BFS1 {
    public static boolean getDirections(int[][] matrix, int from, int to) {
        // TODO:
        // 한 정점에서 다른 정점으로 이어지는 길이 존재하는지 반환.
        // 이중 for문으로 행렬을 순회하면서, 길이 존재하는지 확인.
        Queue<Integer> output = new LinkedList<>();
        boolean[] no = new boolean[matrix.length];
        output.add(from);

        while(output.size() > 0){
            int now = output.poll();
            no[now] = true;

            for (int j = 0; j < matrix.length; j++){
                // (경로 -> to) == 1이면 true
                if (matrix[now][to] == 1){
                    return true;
                }
                // (경로 -> j) == 1이고, 왔던길로 돌아가지 않을 때 다음경로로 추가한다.
                if (matrix[now][j] == 1 && !no[j]){
                    output.add(j);
                    no[j] = true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args){
        boolean result = getDirections(new int[][]
                        {
                                {0, 1, 0, 0},
                                {0, 0, 1, 0},
                                {0, 0, 0, 1},
                                {0, 1, 0, 0}
                        },
                0, 2);
        System.out.println(result);
    }
}
