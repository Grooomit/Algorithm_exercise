package Algorithm_exercise.BFS;

import java.util.ArrayList;
import java.util.Stack;

public class treeDFS {
    public static void main(String[] args) {
        treeDFS.tree roots = new treeDFS.tree("1");
        treeDFS.tree rootChild1 = roots.addChildNode(new treeDFS.tree("2"));
        treeDFS.tree rootChild2 = roots.addChildNode(new treeDFS.tree("3"));
        treeDFS.tree leaf1 = rootChild1.addChildNode(new treeDFS.tree("4"));
        treeDFS.tree leaf2 = rootChild1.addChildNode(new treeDFS.tree("5"));
        ArrayList<String> output = dfs(roots);
        System.out.println(output); // --> ["1", "2", "4", "5", "3"]

        leaf1.addChildNode(new treeDFS.tree("6"));
        rootChild2.addChildNode(new treeDFS.tree("7"));
        output = dfs(roots);
        System.out.println(output); // --> ["1", "2", "4", "6", "5", "3", "7"]
    }
    public static ArrayList<String> dfs(tree node) {
        // TODO:
        // 깊이우선탐색DFS => Stack 각 노드에 접근
        ArrayList<String> output = new ArrayList<>();
        Stack<tree> depth = new Stack<>();

        // Stack에 노드 추가.
        depth.push(node);

        while(!depth.empty()){
            // Stack을 나온 노드는 배열에 추가
            output.add(depth.peek().value);
            tree now = depth.pop();

            // 노드의 childnode를 스택에 추가
            if(now.getChildrenNode() != null){
                for (int i = now.getChildrenNode().size()-1; i >= 0; i--){
                    depth.push(now.getChildrenNode().get(i));
                }
            }
        }
        // Stack을 나온 노드의 자식노드를 Stack에 추가.
        return output;
    }

    //아래 클래스의 내용은 수정하지 말아야 합니다.
    public static class tree {
        private String value;
        private ArrayList<tree> children;

        public tree(String data) {
            this.value = data;
            this.children = null;
        }

        public tree addChildNode(tree node) {
            if(children == null) children = new ArrayList<>();
            children.add(node);
            return children.get(children.size() - 1);
        }

        public String getValue() {      //현재 노드의 데이터를 반환
            return value;
        }

        public ArrayList<tree> getChildrenNode() {
            return children;
        }
    }
}
