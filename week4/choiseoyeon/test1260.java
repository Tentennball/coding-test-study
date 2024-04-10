import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class test2251 {
    static boolean isVisited[][][];
    static int A, B, C;
    
    static ArrayList<Integer>list = new ArrayList<>();
    static ArrayList<int[]>ans = new ArrayList<>();
    static Queue<int[]> q = new LinkedList<>();
    

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        isVisited = new boolean[A+1][B+1][C+1];
        
        q.add(new int[] {0,0,C});	// C의 용량만 가득차있음
        bfs();
        
        Collections.sort(list);	// 오름차순으로 출력
        for(int i=0; i<list.size(); i++) {
            System.out.print(list.get(i)+" ");
        }
    }
    public static void bfs() {
    	while(!q.isEmpty()) {
            int[]node = q.poll();
            
            if(isVisited[node[0]][node[1]][node[2]]) {
                continue;
            }
            
            if(node[0]==0) {	// A 물통이 비었을 경우
                list.add(node[2]);
            }
            
            
            isVisited[node[0]][node[1]][node[2]] = true;
            
            if(node[0]+node[1]<=A) {
                q.add(new int[] {node[0]+node[1], 0, node[2]});
            }
            else {
                q.add(new int[] {A ,node[1]+node[0]-A, node[2]});
            }
            if(node[0]+node[2]<=A) {
                q.add(new int[] {node[0]+node[2],node[1],0});
            }
            else {
                q.add(new int[] {A,node[1],node[2]+node[0]-A});
            }
            if(node[1]+node[0]<=B) {
                q.add(new int[] {0,node[0]+node[1],node[2]});
            }
            else {
                q.add(new int[] {node[0]+node[1]-B,B,node[2]});
            }
            if(node[1]+node[2]<=B) {
                q.add(new int[] {node[0],node[1]+node[2],0});
            }
            else {
                q.add(new int[] {node[0],B,node[2]+node[1]-B});
            }
            if(node[2]+node[0]<=C) {
                q.add(new int[] {0,node[1],node[2]+node[0]});
            }
            else {
                q.add(new int[] {node[0]+node[2]-C,node[1],C});
            }
            if(node[2]+node[1]<=C) {
                q.add(new int[] {node[0],0,node[2]+node[1]});
            }
            else {
                q.add(new int[] {node[0],node[1]+node[2]-C,C});
            }
        }
    }
}
