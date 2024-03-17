import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class test2941 {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		StringBuilder sb = new StringBuilder(input);
		
		int cnt = 0;
		for(int i = 0; i < sb.length(); i++) {
			if(sb.charAt(i)=='c') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='=' || sb.charAt(i+1)=='-') 
						i++;
				}
			}
			else if(sb.charAt(i)=='d') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='z') {
						if(i < sb.length() -2) {
							if(sb.charAt(i+2)=='=')
								i+=2;
						}
					}
					else if(sb.charAt(i+1)=='-')
						i++;
				}
				
			}
			else if(sb.charAt(i)=='l') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='j') 
						i++;
				}
			}
			else if(sb.charAt(i)=='n') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='j') 
						i++;
				}
			}
			else if(sb.charAt(i)=='s') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='=') 
						i++;
				}
			}
			else if(sb.charAt(i)=='z') {
				if(i < sb.length() -1) {
					if(sb.charAt(i+1)=='=') 
						i++;
				}
			}
			cnt++;
		}
		System.out.println(cnt);
	}
}