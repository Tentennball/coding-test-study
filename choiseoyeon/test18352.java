import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class test18352 {
	
	static final int INF = -1;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int X = Integer.parseInt(st.nextToken());
		
		ArrayList<Integer>[] graph = new ArrayList[N+1];
		
		for(int i = 1; i <= N; i++)
			graph[i] = new ArrayList<Integer>(); 
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			graph[a].add(b);
		}
		
		int[] distance = new int[N+1];
        Arrays.fill(distance, INF);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(X);
        distance[X] = 0;

        List<Integer> answer = new ArrayList<>();

        while (!q.isEmpty()) {
            int cur = q.poll();
            if (distance[cur] > K) break;
            if (distance[cur] == K) answer.add(cur);

            for (int next : graph[cur]) {
                if (distance[next] != INF) continue;
                distance[next] = distance[cur]+1;
                q.add(next);
            }
        }

        Collections.sort(answer);
        StringBuilder sb = new StringBuilder();
        for (int cur : answer) {
            sb.append(cur).append('\n');
        }

        System.out.print(answer.isEmpty() ? -1 : sb);

	}

}
