import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution {
	static int T, N, ans;
	static int company[], home[], customer[][];
	static int A[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	
	static void swap(int a[], int k, int i)
	{
		int t = a[k]; a[k] = a[i]; a[i] = t;
	}
	static int getD(int x1, int y1, int x2, int y2)
	{
		return Math.abs(x1 - x2) + Math.abs(y1 - y2);
	}
	
	static void calc() {
		int dist = 0;
		for(int i=0; i < N-1; i++) {
			dist += getD(customer[A[i]][0], customer[A[i]][1], customer[A[i+1]][0], customer[A[i+1]][1]);
		}
		dist += getD(company[0], company[1], customer[A[0]][0], customer[A[0]][1]);
		dist += getD(home[0], home[1], customer[A[N-1]][0], customer[A[N-1]][1]);
		
		if(ans > dist) ans = dist;
	}
	static void perm(int n, int k)
	{
		if(k == n) {
			calc();
//			for(int i=0; i<n; i++)
//				System.out.print(A[i] + " ");
//			System.out.println();
				
		}
		else
		{
			for(int i = k; i < n; i++) {
				swap(A, k, i);
				perm(n, k + 1);
				swap(A, k, i);
			}
		}
			
		
	}
	public static void main(String[] args) throws FileNotFoundException 
	{
		System.setIn(new FileInputStream("src/최적경로_input.txt"));
		Scanner sc = new Scanner(System.in);

		
		T = sc.nextInt();

		for(int tc=0; tc < T; tc++)
		{
			N = sc.nextInt();
			ans = 0x7fffffff;		
			company = new int[2];
			home = new int[2];
			customer = new int[N][2];
			
			//input 
			company[0] = sc.nextInt();
			company[1] = sc.nextInt();
			home[0] = sc.nextInt();
			home[1] = sc.nextInt();
			
			for(int i=0; i < N; i++)
			{
				customer[i][0] = sc.nextInt();
				customer[i][1] = sc.nextInt();
			}
			
			perm(N, 0);
			
			System.out.println("#" + (tc+1) + " " + ans);
			
		}
	}

}
