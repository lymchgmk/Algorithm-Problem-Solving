// {1,2,3} 모든 부분 집합 출력하기


public class PowerSet {
	static int N, A[], data[]= {1,2,3};
	
	static void powerset(int n, int k)
	{
		if(n == k)
		{
			for(int i=0; i<n; i++)
				if(A[i] ==  1) 
					System.out.print(data[i] + " ");
			System.out.println();
		}
			
		else {
			A[k] = 1;
			powerset(n, k + 1);
			A[k] = 0;
			powerset(n, k + 1);
		}
	}
	public static void main(String[] args) {
		N = 3;
		A = new int[N];
		
		powerset(N, 0);
	}
}
