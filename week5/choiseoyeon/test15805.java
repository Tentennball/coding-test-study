import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class test15805 {

	public static void main(String[] args) throws IOException {
		
		TreeSet<Integer> tree = new TreeSet<>();
		int [] arr = new int [200001];
		int [] parent = new int [200001];
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		parent[arr[0]] = -1;
		tree.add(arr[0]);
		
		for(int i = 1; i < N; i++) {
			int value = arr[i];
			
			if(!tree.contains(value)) {
				parent[value]=arr[i-1];
				tree.add(value);
			}
			
		}
		
		System.out.println(tree.size());
		for(int i = 0; i < tree.size(); i++) {
			System.out.print(parent[i]+" ");
		}
	}
}
