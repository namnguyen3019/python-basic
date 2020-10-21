public class Main {
	public static void main(String[] args) {
		int[] intArray = { 1, 3, 3, 0, 1, 4, 4, 2, 8, 10, 20, 11, 15};

		mergeSort(intArray);
		for(int i = 0; i< intArray.length; i++){
			System.out.println(intArray[i]);
		}

	}
	public static void mergeSort(int[] array){
			int n = array.length;
			if(n < 2){
				return;
			}
			int mid = n/2;
			int[] left = new int[mid];
			int[] right = new int[n-mid];
			for(int i = 0; i < mid; i++){
				left[i] = array[i];
			}
			for(int j = mid; j < n; j++){
				right[j-mid] = array[j];
			}

			mergeSort(left);
			mergeSort(right);
			merge(left, right, array);
	}

	public static void merge(int[] left, int[] right, int[] array){
		int i = 0;
		int j = 0;
		int k = 0;

		while( i < left.length && j < right.length){
			if(left[i] > right[j]){
				array[k] = left[i];
				i++;
			}else{
				array[k] = right[j];
				j++;
			}
			k++;
		}
		while(i < left.length){
			array[k]= left[i];
			k++;
			i++;
		}
		while( j < right.length){
			array[k] = right[j];
			j++;
			k++;
		}
	}
}
