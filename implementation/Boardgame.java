package Algorithm_exercise.Implementation;

public class Boardgame {
    public static void main(String[] args){
        int[][] board1 = new int[][]{
                {0, 0, 0, 1},
                {1, 1, 1, 0},
                {1, 1, 0, 0},
                {0, 0, 0, 0}
        };
        int output1 = boardGame(board1, "RRDLLD");
        System.out.println(output1); // 4

        int[][] board2 = new int[][]{
                {0, 0, 1},
                {1, 1, 1},
                {1, 0, 0}
        };
        int output2 = boardGame(board2, "UUUDD");
        System.out.println(output2); // -1

        int[][] board3 = new int[][]{
                {0, 0, 0, 0, 0},
                {0, 0, 1, 0, 0},
                {0, 0, 0, 0, 0},
                {0, 0, 0, 1, 0},
                {0, 0, 0, 0, 0}
        };
        int output3 = boardGame(board3, "DDRRRUDUDUD");
        System.out.println(output3); // 0
    }

    // 말을 조작하여 말이 이동한 좌표값만큼 점수를 얻는다.
    public static Integer boardGame(int[][] board, String operation) {
        // TODO:
        // U(up),D(down),L(left),R(right) 로 말을 조작할 수 있다.
        // x, y 좌표값과 점수 변수 선언
        int x = 0;
        int y = 0;
        int score = 0;
        // operation을 for문으로 순회하면서, 좌표값을 수정한다.
        for (int i = 0; i < operation.length(); i++) {
            if(operation.charAt(i) == 'U') x -= 1;
            else if(operation.charAt(i) == 'D') x += 1;
            else if(operation.charAt(i) == 'L') y -= 1;
            else if(operation.charAt(i) == 'R') y += 1;

            // if 위치한 좌표가 보드 안에 있을 때, 해당 배열값을 score에 더한다.
            if (x >= 0 && y >= 0 && x < board.length && y < board.length){
                score += board[x][y];
            }
            // else 이동한 좌표가 보드밖이면 null 반환
            else {
                return -1;
            }
        }

        return score;
    }
}
