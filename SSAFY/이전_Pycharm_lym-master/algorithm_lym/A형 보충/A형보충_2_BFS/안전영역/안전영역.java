
/*
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
5
 */
import java.util.*;
//import java.io.*;

class Solution
{
	static class Point
	{
		int x;
		int y;
		public Point(int x, int y)
		{
			this.x = x;
			this.y = y;
		}
	}
	static int[][] arr;
	static boolean[][] visited;
	static int ans ;
	static int N;
	static int maxV = Integer.MIN_VALUE;
	static Queue<Point> Q;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static void bfs(int x, int y, int k)
	{
		int nx, ny;
		
		Q.add(new Point(x, y));		
		visited[x][y] = true;
		
		while(!Q.isEmpty())
		{
			Point p = Q.poll();
			x = p.x;
			y = p.y;
			
			for(int i=0; i<4; i++)
			{
				nx = x + dx[i];
				ny = y + dy[i];
				if(nx < 0 || nx >= N ) continue;
				if(ny < 0 || ny >= N ) continue;
				if(visited[nx][ny] == true) continue;
				if(arr[nx][ny] > k)
				{
					Q.add(new Point(nx, ny));		
					visited[nx][ny] = true;				
				}				
			}						
		}		
	}
	public static void main(String args[]) 
	{
		Scanner sc = new Scanner(System.in);
		ans = 1;
		N = sc.nextInt();
		arr = new int[N][N];
		visited = new boolean[N][N];
		Q = new LinkedList<>();
		
		for(int i = 0; i < N; i++)
		{
			for(int j = 0; j < N; j++) {
				arr[i][j] = sc.nextInt();
				if(maxV < arr[i][j]) maxV= arr[i][j];
			}
		}
		
		for (int k = 1; k <= maxV; k++) {
			int cnt = 0;
			for(int i = 0; i < N; i++)
			{
				for(int j = 0; j < N; j++) {
					visited[i][j] = false;
				}
			}
			
			for(int i = 0; i < N; i++)
			{
				for(int j = 0; j < N; j++) {
					if(visited[i][j] == false && arr[i][j] > k) {
						bfs(i, j, k);
						cnt++;
					}
				}
					
			}
			if (ans < cnt) ans = cnt;
		}
		
		System.out.println(ans);

	}
}
