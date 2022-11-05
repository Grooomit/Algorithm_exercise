import java.util.ArrayList;
import java.util.List;

public class Game369 {

    /*
    * 숫자의 각 자릿수를 List 로 변환한다.
    * parameter : int (number)
    * return : List<Integer> (numList)
    * */
    public static List<Integer> toList(int x) {
        List<Integer> numList = new ArrayList<>();
        while(x != 0) {
            numList.add(x % 10);
            x = x / 10;
        }
        return numList;
    }

    /*
    * numList 가 입력됐을 때 손벽을 몇번 쳐야하는지 횟수를 세는 함수
    * parameter : List<Integer> (numList)
    * return : int (count)
    * */
    public static int clapNum(List<Integer> numList) {
        int count = 0;
        for (int num : numList) {
            if (num != 0 && num % 3 == 0) count++;
        }
        return count;
    }

    /*
    * 1부터 number 까지 손뼉을 몇 번 쳐야 하는지 횟수를 측정하는 함수
    * parameter : int (number)
    * return : int (count)
    * */
    public static int solution(int number) {
        int count = 0;
        for (int i = 1; i <= number; i++) {
            count += clapNum(toList(i));
        }
        return count;
    }
}
