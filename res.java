import java.io.BufferedReader;
import java.io.InputStreamReader;

public class reve {

	public static void main(String[] args) throws Exception{
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		String []li=br.readLine().split(" ");
		for(int i=li.length-1;i>=0;i--) {
			System.out.println(li[i]);
		}
	}

}
