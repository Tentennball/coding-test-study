import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test1182 {
	
	static int N, S, cnt = 0;
	static int[]arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());


		st = new StringTokenizer(br.readLine(), " ");
		arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		dfs(0,0);
		
		System.out.println(cnt);
	}
	
	public static void dfs(int index, int sum) {
		if(sum == S && index !=0)
			cnt++;
		for(int i = index; i < N; i++) {
			int temp = sum + arr[i];
			dfs(i+1, temp);
		}
	}
}
