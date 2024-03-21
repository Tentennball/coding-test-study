import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class test2751 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		
		List<Integer>list = new ArrayList<Integer>();
		
		for(int i = 0; i < N; i++) {
			list.add(scanner.nextInt());
		}
		
		Collections.sort(list);
		

		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < N; i++) {
			sb.append(list.get(i)).append("\n");
		}
		
		System.out.println(sb);
		
		scanner.close();
	}

}
