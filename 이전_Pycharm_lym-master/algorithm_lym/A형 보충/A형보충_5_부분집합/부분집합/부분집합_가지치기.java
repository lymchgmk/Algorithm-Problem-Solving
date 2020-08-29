
public class PowerSet2 {
	static int N, A[], data[]= {1,2,3,4,5,6,7,8,9,10};
	static int count, total;
	static void printSet(int n, int sum)
	{
		if(sum == 10) {		
			for(int i=0; i<n; i++)
				if(A[i] ==  1) 
					System.out.print(data[i] + " ");
			System.out.println();
		}
	}
	
	static void powerset(int n, int k, int sum)
	{
		if(sum > 10) return;
		
		if(n == k)
			printSet(n, sum);
		else {
			A[k] = 1;
			powerset(n, k + 1, sum + data[k]);
			A[k] = 0;
			powerset(n, k + 1, sum);
		}
	}
	
	public static void main(String[] args) {
		N = 10;
		A = new int[N];
		
		powerset(N, 0, 0);
	}
}
