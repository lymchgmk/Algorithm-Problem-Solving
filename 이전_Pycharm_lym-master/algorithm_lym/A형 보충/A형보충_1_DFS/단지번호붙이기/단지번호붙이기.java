import java.io.FileInputStream;
import java.util.*;

public class Main
{
	static int N;   //정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25
	static int[][] map;
	static boolean[][] visited; 
	static int group;
	static int dx[] = {-1, 1, 0, 0};
	static int dy[] = {0, 0, -1, 1};
	static int count[];
	
	static void dfs(int x, int y, int group)
	{
		int nx, ny;
		visited[x][y] = true;
		map[x][y] = group;
		count[group]++;
		
		for(int i=0; i<4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			
			if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
			if(visited[nx][ny]) continue;
			if(map[nx][ny] == 0) continue;
			dfs(nx, ny, group);		
		}
	}
	static void printArr(int map[][])
	{
		for(int i=0; i < N; i++) {
			for(int j=0; j < N; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void main(String args[]) 
	{

		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N][N];
		visited = new boolean[N][N];
		group = 1;
		count = new int[N*N+1];
		String input;
		
		for(int i=0; i < N; i++) {
			input = sc.next();
			for(int j=0; j < N; j++) {
				map[i][j] = input.charAt(j) - '0';
			}
		}
		
		//printArr(map);
		
		for(int i=0; i < N; i++) {
			for(int j=0; j < N; j++) {
				if(map[i][j] != 0 && visited[i][j] == false)
				{
					dfs(i, j, group);
					group++;
				}
			}
		}
		//printArr(map);

		System.out.println(group-1);
		Arrays.sort(count);
		for(int i : count)
			if(i != 0)
				System.out.println(i);

		sc.close();
	}
}
