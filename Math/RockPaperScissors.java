package Algorithm_exercise.Math;

import java.util.ArrayList;
import java.util.Arrays;

public class RockPaperScissors {
        public ArrayList<String[]> rockPaperScissors(int rounds) {
            //결과를 담을 ArrayList를 선언합니다.
            ArrayList<String[]> outcomes = new ArrayList<>();
            // 함수를 실행하여 반환된 결과를 다시 반환합니다.
            return permutation(rounds, new String[]{}, outcomes);
        }

        // 재귀를 사용할 함수 선언

        public ArrayList<String[]> permutation(int roundsToGo, String[] playedSoFar, ArrayList<String[]> outcomes) {
            // rounds가 0일 경우 outcones 배열에 삽입하고, 재귀에서 빠져나옵니다.
            if(roundsToGo == 0) {
                outcomes.add(playedSoFar);
                return outcomes;
            }

            String[] rps = new String[]{"rock", "paper", "scissors"};

            // rps 배열을 한 번씩 순회합니다.
            for(int i = 0; i < rps.length; i++) {
                // rps의 i번째 요소를 변수에 담아서
                String currentPlay = rps[i];

                // permutate(본인)에 기존 rounds에서 하나 뺀 숫자와, 일회용 배열 playedSoFar에 currentPlay를 삽입하여 재귀를 실행합니다.
                // rounds에서 하나를 빼는 이유는, 일회용 배열의 크기를 rounds만큼 맞춰주기 위함입니다. [rock, rock, rock]
                String[] concatArray = Arrays.copyOf(playedSoFar, playedSoFar.length + 1);  //배열의 크기를 하나 늘리고, currentPlay를 요소로 넣어줍니다.
                concatArray[concatArray.length - 1] = currentPlay;

                outcomes = permutation(roundsToGo - 1, concatArray, outcomes);
            }

            // outcomes를 반환합니다.
            return outcomes;
        }
    }


