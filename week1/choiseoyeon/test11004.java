import java.util.Scanner;

public class test11004 {

public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		int N = scanner.nextInt();
		int K = scanner.nextInt();
		
		int A[] = new int[N];
		
		for(int i = 0; i < N; i++) {
			A[i] = scanner.nextInt();
		}
		
		//Á¤·Ä
		int temp = A[0];
		for(int i = 1; i < N; i++) {
            temp = A[i];
            for(int j=1; j >= 0 && (A[j] > temp); j--)
                A[j+1] = A[j];
                    
            A[i+1] = temp;
		}
		System.out.println(A[K-1]);

		scanner.close();
	}

}
