import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.io.FileInputStream;

public class BFS {
	static int V, E, G[][], vistied[];
	static Queue<Integer> Q;
	static void bfs(int v)
	{
		Q.add(v);	
		vistied[v] = 1;
		System.out.print(v + " ");
		
		while(!Q.isEmpty())
		{
			v = Q.poll();
			for(int w=1; w < V+1; w++)
			{
				if(G[v][w] == 1 && vistied[w] == 0)
				{
					Q.add(w);
					vistied[w] = 1;
					System.out.print(w + " ");
					
				}
			}
		}
		
	}
	
	
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		System.setIn(new FileInputStream("src/dfs_input.txt"));
		Scanner sc = new Scanner(System.in);
		
		V = sc.nextInt();
		E = sc.nextInt();
		
		G = new int[V+1][V+1];
		vistied = new int [V+1];
		Q = new LinkedList<>();	
		
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
		
		bfs(1);
	}

}
