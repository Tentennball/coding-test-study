import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.InputStreamReader;
import java.io.IOException;

public class test1546 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		double[]arr = new double[N];
		
		double max = 0;
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if(arr[i] >= max)
				max = arr[i];
		}
		
		double sum = 0;
		for(int i = 0; i < N; i++) {
			arr[i] = arr[i]/max*100;
			sum += arr[i];
		}
		System.out.println(sum/N);
		
	}
}