import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        if(T>100){
            System.out.println("Steam");
        }
        else if(T<0){
            System.out.println("Ice");
        }
        else if(0<=T && T<=100){
            System.out.println("Water");
        }
    }
}