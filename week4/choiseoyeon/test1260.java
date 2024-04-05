import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class test1260 {
	
	static ArrayList<Integer>[] arr;
	static boolean[] isVisited; 

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());
		
		arr = new ArrayList[N+1];
		isVisited = new boolean[N+1];
		
		for(int i = 1; i <= N; i++) {
			arr[i] = new ArrayList<Integer>();
		}
		//Arrays.fill(isVisited, false);
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			arr[a].add(b);	//양방향 
			arr[b].add(a);
		}
		
		DFS(V);
		Arrays.fill(isVisited, false);	//초기화
		System.out.println();
		BFS(V);
		
		
	}
	
	private static void DFS(int V) {
		if(isVisited[V])	// 방문한 노드일 경우
			return;
		
		System.out.print(V+" ");
		isVisited[V] = true;
		
		for(int i = 0; i < arr[V].size(); i++) {
			int min = 1001;	// 정점의 개수 1000
			
			for(int j = 0; j < arr[V].size(); j++) {
				int temp = arr[V].get(j);
				
				if(!isVisited[temp])
					min = Math.min(min, temp);
			}
			
			if(min == 1001)
				break;
			DFS(min);	
		}
	}
	
	private static void BFS(int V) {
		Queue<Integer> BFS = new LinkedList<Integer>();
		BFS.offer(V);
		isVisited[V] = true;
		
		while(!BFS.isEmpty()) {
			int node = BFS.poll();	// BFS의 헤드값(부모) 가져오고 제거
			System.out.print(node+" ");
			
			for(int i = 0; i < arr[node].size(); i++) {
				int min = 1001;
				
				for(int j = 0; j < arr[node].size(); j++) {
					int temp = arr[node].get(j);
					
					if(!isVisited[temp])
						min = Math.min(min, temp);
				}
				
				if(min == 1001)
					break;
				
				BFS.add(min);
				isVisited[min] = true;
			}
		}
	}
}
