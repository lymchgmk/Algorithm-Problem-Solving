import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Solution2 {
	static int T, N, ans;
	static int A[], Pos[][], Dist[][];
	
	static void swap(int a[], int k, int i)
	{
		int t = a[k]; a[k] = a[i]; a[i] = t;
	}
	static int getD(int x1, int y1, int x2, int y2)
	{
		return Math.abs(x1 - x2) + Math.abs(y1 - y2);
	}
	
	static void perm(int n, int k, int cur_dist)
	{
		if(cur_dist > ans) return;   //가지치기
		
		if(k == n) {
			cur_dist += Dist[A[k]][A[N+1]]; //마지막고객 -> 집
			if(cur_dist < ans) ans = cur_dist; 	
		}
		else
		{
			for(int i = k; i < n; i++) {
				swap(A, k+1, i+1);
				perm(n, k + 1, cur_dist + Dist[A[k]][A[k+1]]);
				swap(A, k+1, i+1);
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
					
			A = new int[N+2];
			Pos = new int[N+2][2];
			Dist = new int[N+2][N+2];
			
			ans = 0x7fffffff;
			
			for(int i=0; i<N+2; i++) 
				A[i] = i;
			
			//회사
			Pos[0][0] = sc.nextInt();
			Pos[0][1] = sc.nextInt();
			//집
			Pos[N+1][0] = sc.nextInt();
			Pos[N+1][1] = sc.nextInt();
			
			//고객
			for(int i=1; i <= N; i++)
			{
				Pos[i][0] = sc.nextInt();
				Pos[i][1] = sc.nextInt();
			}
			
			//거리 미리 계산
			for(int i=0; i < N+1; i++)
				for(int j=i+1; j < N+2; j++)
					Dist[i][j] = Dist[j][i] = getD(Pos[i][0], Pos[i][1], Pos[j][0], Pos[j][1]);
			
			perm(N, 0, 0);
			
			System.out.println("#" + (tc+1) + " " + ans);
			
		}
	}

}
