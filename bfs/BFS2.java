package Algorithm_exercise.BFS;

import java.util.Stack;

public class BFS2 {
    public static int connectedVertices(int[][] edges) {
        // TODO:
        // edges 배열 순회하면서 정점갯수 파악
        int num = 0;
        for (int i = 0; i < edges.length; i++) {
            if (num < edges[i][0]) num = edges[i][0];
            if (num < edges[i][1]) num = edges[i][1];
        }

        // 정점갯수 사이즈의 2차원배열 생성
        int[][] matrix = new int[num + 1][num + 1];

        // edges 배열 순회하면서 2차원 간선배열 작성
        for (int i = 0; i < edges.length; i++) {
            matrix[edges[i][0]][edges[i][1]] = 1;
            matrix[edges[i][1]][edges[i][0]] = 1;
        }

        // boolean[], Stack, now 변수 생성
        boolean[] value = new boolean[num + 1];
        Stack<Integer> next = new Stack<>();
        int now = 0;
        num = 0;

        // for문으로 boolean[] false인 정점선택 후 DFS 진행
        for (int i = 0; i < matrix.length; i++) {
            if (!value[i]) {
                next.push(i);

                // Stack 크기가 0이 아닐때 반복
                while (next.size() > 0) {
                    now = next.pop();
                    value[now] = true;

                    for (int j = 0; j < matrix[now].length; j++) {
                        if (matrix[now][j] == 1 && !value[j]) {
                            next.push(j);
                            value[j] = true;
                        }
                    }
                }
                num++;
            }
        }
        return num;
    }

    public static void main(String[] args){

        int result = connectedVertices(new int[][]{
                {0, 1},
                {2, 3},
                {4, 5},
        });
        System.out.println(result); // 3

        result = connectedVertices(new int[][]{
                {0, 1},
                {2, 3},
                {3, 4},
                {3, 5},
        });
        System.out.println(result); // 2

    }
}
