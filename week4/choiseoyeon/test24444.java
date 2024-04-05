import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class test24444 {

	static List<List<Integer>> arr = new ArrayList<>();
	static int isVisited[];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		isVisited = new int[N+1];
		
		for(int i = 0; i <= N; i++) {
			arr.add(new ArrayList<>());
		}
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			arr.get(a).add(b);	//¾ç¹æÇâ 
			arr.get(b).add(a);
		}
		for(int i = 1; i<=N; i++)
            Collections.sort(arr.get(i));
		
		BFS(R);
		
		for(int i = 1; i<=N; i++)
            System.out.println(isVisited[i]);
	}
	
	private static void BFS(int R) {
		Queue<Integer> BFS = new LinkedList<Integer>();
		int cnt = 1;

		BFS.offer(R);
		isVisited[R] = cnt++;

        while(!BFS.isEmpty()){
            int a = BFS.poll();

            for(int i = 0; i< arr.get(a).size(); i++){
                int node = arr.get(a).get(i);

                if(isVisited[node] != 0)
                    continue;

                BFS.offer(node);
                isVisited[node] = cnt++;
            }
        }
		
	}
}
