import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class test1058 {
	
	static final int INF = 100000000;
	static int[][] cost = new int [51][51];

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= N; i++) {
			char[] str = br.readLine().toCharArray();
			
			for(int j = 1; j <= N; j++) {
				if(i==j) 
					continue;
				if (str[j-1] == 'Y')
					cost[i][j] = 1;
				else
					cost[i][j] = INF;
			}
		}

		for(int i = 1; i <= N; i++)
			for(int j = 1; j <= N; j++)
				for(int k = 1; k <= N; k++) {
					if(j==k)continue;
					
					cost[i][j] = Math.min(cost[i][j], cost[i][k] + cost[k][j]);	
				}
		int max = 0;
        for(int i = 1; i <= N; i++) {
            int cnt = 0;

            for (int j = 1; j <= N; j++)
                if (cost[i][j] == 2 || cost[i][j] == 1) // 唱客 模备, 模备狼 模备
                	cnt++;
            max = Math.max(max, cnt);
        }

        System.out.println(max);
	}

}
