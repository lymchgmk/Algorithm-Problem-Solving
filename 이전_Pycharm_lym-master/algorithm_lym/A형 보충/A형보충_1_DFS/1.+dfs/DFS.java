import java.util.Scanner;
import java.io.FileInputStream;
public class DFS {
	static int V, E, G[][], vistied[];
	static void dfs(int v)
	{
		vistied[v] = 1;
		System.out.print(v + " ");
		
		for(int w=1; w <=V; w++) 
		{
			if(G[v][w] == 1 && vistied[w] == 0)
				dfs(w);
		}
		
	}
	
	public static void main(String args[]) throws Exception
	{
		System.setIn(new FileInputStream("src/dfs_input.txt"));
		Scanner sc = new Scanner(System.in);
		
		//int V, E, G[][], vistied[];
		
		V = sc.nextInt();
		E = sc.nextInt();
		
		G = new int[V+1][V+1];
		vistied = new int [V+1];
		
		for(int i=0; i < E; i++)
		{
			int from = sc.nextInt();
			int to = sc.nextInt();
			
			G[from][to] = 1;
			G[to][from] = 1;
		}
		
		/* 입력확인 */
		for(int i=1; i <= V; i++)
		{		
			System.out.print(i + " : "); 
			for(int j = 0; j <= V; j++)
			{
				System.out.print(G[i][j] +" ");
			}
			System.out.println();
		}	
		
		dfs(1);
	}
}
