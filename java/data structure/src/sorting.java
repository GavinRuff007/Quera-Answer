
            

import java.util.Arrays;
//O(n^2):
public class sorting {
    static void bubbleSort(int[] arr) {  
        int n = arr.length;  
        int temp = 0;  
         for(int i=0; i < n; i++){  
                 for(int j=1; j < (n-i); j++){  
                          if(arr[j-1] > arr[j]){                                    
                                 temp = arr[j-1];  
                                 arr[j-1] = arr[j];  
                                 arr[j] = temp;  
                         }     
                 }  
         }
        System.out.println(Arrays.toString(arr));   
    }
    
//O(n^2):
public static void SelectionSort(int[] arr)
{
  int smallest;
  for (int i = 0; i <arr.length - 1; i++)
  {
    smallest = i;
    for (int j = i + 1; j < arr.length; j++)
    {
      if (arr[j] < arr[smallest])
      {
        smallest = j;
      }
    }
    int temp = arr[i];
    arr[i] = arr[smallest];
    arr[smallest] = temp; 
  }
  System.out.println(Arrays.toString(arr));  
}
    
//O(n^2): 
    public static void insertionSort(int array[]) {  
        int n = array.length;  
        for (int j = 1; j < n; j++) {  
            int key = array[j];  
            int i = j-1;  
            while ( (i > -1) && ( array [i] > key ) ) {  
                array [i+1] = array [i];  
                i--;  
            }  
            array[i+1] = key;  
        }  
    }  
       
   
   
    
    


//O(nlogn): 
public static void mergeSort(int[] a, int n) {
    if (n < 2) {
        return;
    }
    int mid = n / 2;
    int[] l = new int[mid];
    int[] r = new int[n - mid];
 
    for (int i = 0; i < mid; i++) {
        l[i] = a[i];
    }
    for (int i = mid; i < n; i++) {
        r[i - mid] = a[i];
    }
    mergeSort(l, mid);
    mergeSort(r, n - mid);
 
    merge(a, l, r, mid, n - mid);
    
}
public static void merge(
  int[] a, int[] l, int[] r, int left, int right) {
 
    int i = 0, j = 0, k = 0;
    while (i < left && j < right) {
        if (l[i] <= r[j]) {
            a[k++] = l[i++];
        }
        else {
            a[k++] = r[j++];
        }
    }
    while (i < left) {
        a[k++] = l[i++];
    }
    while (j < right) {
        a[k++] = r[j++];
    }
    System.out.println(Arrays.toString(a)); 
}

public static void heapsort(int arr[])
    {
        int n = arr.length;
        for (int i = n / 2 - 1; i >= 0; i--){
            heapify(arr, n, i);
        }
        for (int i=n-1; i>=0; i--)
        {

            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }
   static  void heapify(int arr[], int n, int i)
    {
        int largest = i;  
        int l = 2*i + 1;  
        int r = 2*i + 2;  
  

        if (l < n && arr[l] > arr[largest])
            largest = l;

        if (r < n && arr[r] > arr[largest])
            largest = r;

        if (largest != i)
        {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;
            heapify(arr, n, largest);
        }
        System.out.println(Arrays.toString(arr)); 
    }

  
  public static void main(String[] args){
      
      int[] a = {12,5,2,7823,2};
      System.out.println("bubbleSort:");  
      bubbleSort(a);
      System.out.println("selectionSort:");  
      SelectionSort(a);
      System.out.println("insertionSort:");  
      insertionSort(a);
      System.out.println("merge-sort:"); 
      int alength = a.length;
      mergeSort(a,alength);
      System.out.println("heap-sort:");  
      heapsort(a);
      System.out.println("we dont say quicksort!!!!!!!!!");
  }
}
