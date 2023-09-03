import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class MultiClientTest {
    public static void main(String[] args) {
        try(ServerSocket s = new ServerSocket(8189)){
            while(true){
                Socket income = s.accept();
                System.out.println("New Connection");
                Runnable run = new ThreadClientHandler(income);
                Thread thread = new Thread(run);
                thread.start();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
    static class ThreadClientHandler implements Runnable{
        private Socket socket;

        public ThreadClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try{
                InputStream input = socket.getInputStream();
                OutputStream output = socket.getOutputStream();
                Scanner in = new Scanner(input,"UTF-8");
                PrintWriter out = new PrintWriter(new OutputStreamWriter(output,"UTF-8"),true);
                out.println("Hello!");
                boolean done = false;
                while(!done && in.hasNextLine()){
                    String Line = in.nextLine();
                    System.out.println(Line);
                    out.println("You entered:"+Line);
                    if (Line.trim().equals("exit")){
                        done = true;
                    }
                }
            }catch (IOException e) {
                throw new RuntimeException(e);
            }

        }
    }

    }


