import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test10025 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int arr[][] = new int[N][2];
		int max_x = 0;
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int g = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			
			arr[i][0] = g;
			arr[i][1] = x;
			if(x > max_x)
				max_x = x;
			/*System.out.println(arr[i][0]);
			System.out.println(arr[i][1]);*/
		}
		
		int sum = 0;
		for(int i = 0; i < max_x; i++) {
			if(arr[i][1] - K)
		}
		
		// arr[i][1] - K, arr[i][1] + K
		
		int max = 0;
		
		
		
	}

}
