public class PowerSet1 {
	static int N, A[], data[]= {1,2,3,4,5,6,7,8,9,10};
	static int count, total;
	static void printSet(int n)
	{
		int sum = 0;
		for(int i=0; i<n; i++)
			if(A[i] ==  1) 
				sum += data[i];
				
		if(sum == 10) {		
			for(int i=0; i<n; i++)
				if(A[i] ==  1) 
					System.out.print(data[i] + " ");
			System.out.println();
		}
	}
	
	static void powerset(int n, int k)
	{
		if(n == k)
			printSet(n);
		else {
			A[k] = 1;
			powerset(n, k + 1);
			A[k] = 0;
			powerset(n, k + 1);
		}
	}
	
	public static void main(String[] args) {
		N = 10;
		A = new int[N];
		
		powerset(N, 0);
	}
}
