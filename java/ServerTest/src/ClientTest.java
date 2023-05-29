
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.Scanner;

public class ClientTest {
    public static void main(String[] args) throws IOException{
        try(Socket s = new Socket(InetAddress.getLoopbackAddress(),8189)){
            Scanner in = new Scanner(s.getInputStream(),"UTF-8");
            PrintWriter out = new PrintWriter(new OutputStreamWriter(s.getOutputStream(),"UTF-8"),true);
            Scanner user = new Scanner(System.in);
            boolean done = false;
            while(!done){
                if(in.hasNext()){
                    System.out.println(in.nextLine());
                    System.out.println("enter:");
                    String msg = user.nextLine();
                    out.println(msg);
                    if(msg.trim().equals("exit")){
                        done = true;
                    }
                }
            }
        }catch(IOException e){
        } 
    }
}
