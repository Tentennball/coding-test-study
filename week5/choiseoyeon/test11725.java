import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class test11725 {
    public static void main(String[] args) throws IOException {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());

        ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
        for (int i = 0; i < N; i++) {
        	tree.add(new ArrayList<>());
        }
            

        for (int i = 0; i < N - 1; i++) {
        	st = new StringTokenizer(br.readLine());
			int node1 = Integer.parseInt(st.nextToken()) - 1;
			int node2 = Integer.parseInt(st.nextToken()) - 1;

            tree.get(node1).add(node2);
            tree.get(node2).add(node1);
        }

        boolean[] isVisited = new boolean[N+1];
        int[] parent = new int[N+1];

        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        isVisited[0] = true;
        while (!queue.isEmpty()) {
            int v = queue.remove();
            for (int node : tree.get(v))
                if (!isVisited[node]) {
                    isVisited[node] = true;
                    queue.add(node);
                    parent[node] = v;
                }
        }

        for (int i = 1; i < N; i++)
            System.out.println(parent[i] + 1);
    }
}