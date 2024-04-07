import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class test1806 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		
		int arr[] = new int[N];
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		int start = 0, end = 0; // 투포인터
		int sum = 0;
		int length = 0, min = 0;
		while(start < N && end < N-1) {
			if(sum >= S) {
				sum -= arr[start++];
				length = end - start + 1;
				min = length;
				if(min > length)
					min = length;
			}
			else if(sum < S)
				sum += arr[++end];
		}
		if(sum < S)
			System.out.println(0);
		else
			System.out.println(min);
	}

}
