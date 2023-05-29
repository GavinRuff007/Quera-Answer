
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.*;
public class ServerTest {
    public static void main(String[] args) {
        try(ServerSocket server = new ServerSocket(8189)){
            try(Socket socket = server.accept()){
                InputStream input = socket.getInputStream();
                OutputStream output = socket.getOutputStream();
                try(Scanner in = new Scanner(input,"UTF-8")) {
                    PrintWriter out = new PrintWriter(new OutputStreamWriter(output, StandardCharsets.UTF_8),true);
                    out.println("Hello pls enter exit to finish.");
                    boolean done = false;
                    while(!done && in.hasNextLine()){
                        String Line = in.nextLine();
                        System.out.println(Line);
                        out.println("You entered:"+Line);
                        if (Line.trim().equals("exit")){
                            done = true;
                        }
                    }
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
