
public class Permultation {
	static boolean flag;
//	static int arr[] = {6,6,6,7,7,7};
//	static int arr[] = {1,2,4,7,8,3};
//	static int arr[] = {0,5,4,0,6,0};
//	static int arr[] = {1,0,1,1,2,3};
	static int arr[] = {1,2,3,4,5,6};
	static void printArr(int[] arr, int n)
	{
		for(int i=0; i<n; i++)
			System.out.print(arr[i] + " ");
		System.out.println();
		
	}
	static void babyGin()
	{
		int check = 0;
		
		if(arr[0] == arr[1] && arr[1] == arr[2]) check++;
		if(arr[3] == arr[4] && arr[4] == arr[5]) check++;
		
		if(arr[0] + 1 == arr[1] && arr[1] + 1 == arr[2]) check++;
		if(arr[3] + 1 == arr[4] && arr[4] + 1 == arr[5]) check++;
		
		if(check == 2) {
			flag = true;
			return;
		}
	}
	static void swap(int[] arr, int x, int y)
	{
		int t= arr[x];
		arr[x] = arr[y];
		arr[y] = t;	
	}
	static void perm(int n, int k)
	{
		if(k == n) {
			printArr(arr, n);
			babyGin();
		}
		else {
			for(int i = k; i < n; i++) {
				swap(arr, k, i);
				perm(n, k + 1);
				swap(arr, k, i);
			}
		}
	}
	
	public static void main(String[] args) {
		flag = false;
		perm(3, 0);

		if(flag) System.out.println("BabyGin");
		else System.out.println("Not BabyGin");
	}

}
