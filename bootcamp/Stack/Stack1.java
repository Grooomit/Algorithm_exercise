package Algorithm_exercise.Stack;
import java.util.*;

public class Stack1 {
    public static void main(String[] args) {

        Stack<String> next = new Stack<>();
        Stack<String> prev = new Stack<>();
        Stack<String> current = new Stack<>();

        String[] actions = new String[]{"B"};
        String start = "A";
        current.push(start);

        for(String str: actions){
            System.out.println(str);
            //앞으로가기 구현
            if(str == "1" && !next.empty()) {
                prev.push(current.pop());
                current.push(next.pop());
            }
            //뒤로가기 구현
            else if(str == "-1" && !prev.empty()){
                next.push(current.peek());
                current.pop();
                current.push(prev.peek());
                prev.pop();
            }

            //새로운 페이지 접속 구현
            if(Character.isUpperCase(str.charAt(0))){
                prev.push(current.pop());
                current.push(str);
                while(!next.empty()){
                    next.pop();
                }
            }
        }
        System.out.println("--------------");
        System.out.println(prev);
        System.out.println(current);
        System.out.println(next);
        System.out.println("--------------");



    }
}
