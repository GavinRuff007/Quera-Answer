import java.util.Scanner;
public class Main {        
    static int is_prime(int n){
        int i,m=0,flag=0;
         i = 2;
         m=(int)(n/2);
        if(n==0||n==1){
           return 0;
        }else{
            while(i<=m){
                if(n%i==0){  
                    flag=1;
                    return 0;
                        } 
                i++;
                }  
            }
            if(flag==0){  
                return 1; 
            }  
        return 0;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        for(int i=a;i<=b;i++){
            if (is_prime(i)==1){
                System.out.println(i);
                
            }
        }
    }
    
}