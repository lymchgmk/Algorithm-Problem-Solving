import java.util.Scanner;

public class Comb {

	static int N, K, T[];
	static int A[]= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	static void myprint()
	{ 
		for(int i = 0; i < K; i++)
			System.out.print(T[i] + " ");
		System.out.println();
	}
	
	static void comb(int n, int r)
	{
		if(r == 0) myprint();
		else if(n < r) return;
		else
		{
			T[r-1] = A[n-1];
			comb(n-1, r-1);
			comb(n-1, r);
		}
		
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		K = sc.nextInt();
		T = new int[K];
		
		comb(N, K);
	}

}
