import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class test21278 {
	static int N,M;
	static final int INF = 100000000;
	static int[][] cost = new int [101][101];

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for(int i = 1; i <= N; i++) {
			for(int j = 1; j <= N; j++) {
				if(i==j) 
					continue;
				cost[i][j] = INF;
			}
		}
		
		for(int i =0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			cost[a][b] = cost[b][a] = 1;
		}
		
		for(int i = 1; i <= N; i++)
			for(int j = 1; j <= N; j++)
				for(int k = 1; k <= N; k++) {
					if(j==k)continue;
					
					cost[i][j] = Math.min(cost[i][j], cost[i][k] + cost[k][j]);	
				}
		
		int point1=Integer.MAX_VALUE;
		int point2=Integer.MAX_VALUE;
		int min=Integer.MAX_VALUE;
		
		for(int i = 1; i <= N; i++) {
			for(int j = i+1; j <= N; j++) {
				int dis = distance(i, j);
				if(min > dis) {
					point1 = i;
					point2 = j;
					min = dis;
				}
			}
		}
		System.out.println(point1+" "+point2+" "+min*2);
	}
	
	
	// 두 치킨 집까지의 거리 중 더 가까운 치킨집까지의 거리 return
	static int distance(int x, int y) {
		
		int result = 0;
		for(int i = 1;i <= N; i++)
			result += Math.min(cost[x][i], cost[y][i]);
		
		return result;
	}

}
