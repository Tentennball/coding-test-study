import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class test24479 {

	static int cnt = 1;
	static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
	static boolean isVisited[];
	static int[] result;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		isVisited = new boolean[N+1];
		result = new int[N+1];
		
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
		
		DFS(R);
		
		for(int i = 1; i<=N; i++)
            System.out.println(result[i]+" ");
	}

	private static void DFS(int R) {
		
		isVisited[R] = true;
		result[R] = cnt++;
		Collections.sort(arr.get(R));
		
		for(Integer value : arr.get(R)) {
			if(!isVisited[value])
				DFS(value);
		}
		return;
	}


}

