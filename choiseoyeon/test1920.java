import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class test1920 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[]list1 = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for(int i = 0; i < N; i++) {
			list1[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(list1);
		
		int M = Integer.parseInt(br.readLine());
		int[]list2 = new int[M];
		st = new StringTokenizer(br.readLine(), " ");
		
		for(int i = 0; i < M; i++) {
			list2[i] = Integer.parseInt(st.nextToken());
			int idx = Arrays.binarySearch(list1, list2[i]);
			if(idx < 0)
				System.out.println(0);
			else
				System.out.println(1);
		}		
	}
}
