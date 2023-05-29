import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static int get(int[] arrayOfInts, int index) {
        return arrayOfInts[index];
    }
    public static void main(String[] args) throws IOException {
        Scanner n = new Scanner(System.in);
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bi.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        int[] array1 = new int[N*M];
        for (int j=0;j<N;j++) {
            String[] strNums1 = bi.readLine().split(" ");
            for (int i = 0; i < M; i++) {
                array1[i + M*j] = Integer.parseInt(strNums1[i]);
            }
        }
        int[] array2 = new int[N*M];
        for (int j=0;j<N;j++) {
            String[] strNums2 = bi.readLine().split(" ");
            for (int i = 0; i < M; i++) {
                array2[i + M*j] = Integer.parseInt(strNums2[i]);
            }
        }
        int[] array3 = new int[N*M];
        for(int i=0;i<N*M;i++){
            array3[i] = array1[i] + array2[i];
        }
        int k =1;
        for(int i=0;i<N*M;i++){
            if(i == M*k){
                System.out.println();
                k++;
            }
            System.out.print(get(array3,i)+" ");
        }
    }
}