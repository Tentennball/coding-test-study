import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test20364 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		int N = Integer.parseInt(st.nextToken());	//땅의 수
		int Q = Integer.parseInt(st.nextToken());	//오리수 
		boolean [] isVisited = new boolean[N+1];
		
		for(int i = 0; i < Q; i++) {
			int num = Integer.parseInt(br.readLine());
			
			int temp = num;
			while(temp > 0) {
				if(temp==1) {
					//System.out.println(0);
					sb.append(0+"\n");
					isVisited[num] = true;
					break;
				}
				else if(isVisited[temp]) {
					//System.out.println(temp);
					sb.append(temp+"\n");
					break;
				}
				else
					temp /= 2;
			}
		}
		System.out.println(sb.toString());
	}
}