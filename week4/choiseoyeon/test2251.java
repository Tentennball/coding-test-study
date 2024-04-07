import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class test2251 {
    static boolean isVisited[][][];
    static ArrayList<Integer>list = new ArrayList<>();
    static Queue<Node> q = new LinkedList<>();
    static int A, B, C;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        isVisited = new boolean[A+1][B+1][C+1];
        
        q.add(new Node(0,0,C));	// C의 용량만 가득차있음
        bfs();
        
        Collections.sort(list);	// 오름차순으로 출력
        for(int i=0; i<list.size(); i++) {
            System.out.print(list.get(i)+" ");
        }
    }
    public static void bfs() {
    	while(!q.isEmpty()) {
            Node node = q.poll();
            if(isVisited[node.a][node.b][node.c]) {
                continue;
            }
            if(node.a==0) {	// A 물통이 비었을 경우
                list.add(node.c);
            }
            isVisited[node.a][node.b][node.c] = true;
            
            if(node.a+node.b<=A) {
                q.add(new Node(node.a+node.b,0,node.c));
            }
            else {
                q.add(new Node(A,node.b+node.a-A,node.c));
            }
            if(node.a+node.c<=A) {
                q.add(new Node(node.a+node.c,node.b,0));
            }
            else {
                q.add(new Node(A,node.b,node.c+node.a-A));
            }
            if(node.b+node.a<=B) {
                q.add(new Node(0,node.a+node.b,node.c));
            }
            else {
                q.add(new Node(node.a+node.b-B,B,node.c));
            }
            if(node.b+node.c<=B) {
                q.add(new Node(node.a,node.b+node.c,0));
            }
            else {
                q.add(new Node(node.a,B,node.c+node.b-B));
            }
            if(node.c+node.a<=C) {
                q.add(new Node(0,node.b,node.c+node.a));
            }
            else {
                q.add(new Node(node.a+node.c-C,node.b,C));
            }
            if(node.c+node.b<=C) {
                q.add(new Node(node.a,0,node.c+node.b));
            }
            else {
                q.add(new Node(node.a,node.b+node.c-C,C));
            }
        }
    }
}
class Node{
    int a,b,c;
    Node(int a, int b ,int c){
        this.a=a;
        this.b=b;
        this.c=c;
    }
}