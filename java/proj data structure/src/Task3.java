import java.util.*;
public class Task3 { 
    public static void main(String args[]) {} 
/*************************************************question-1***********************************************************/        
    
        
        public Stack<Object> insert(char...args){
            Stack<Object> stack1 = new Stack<>();
            stack1.push(args);
            return stack1;
        }
        public  Stack<Object> delete(Stack<Object> stack1){

            Stack<Object> stack2 = new Stack<>();
            if(stack1.isEmpty()){
                    System.out.println("Empty");
           }
           while(stack1.size() > 0){
                Object p = stack1.pop();
                stack2.push(p);
              }
            return stack2;
         } 
/*************************************************question-2***********************************************************/
	Queue<Integer> First1;
	Deque<Integer> First2;
        static Queue<Integer> queue; 
	public Task3(){
		First1 = new LinkedList<>();
		First2 = new ArrayDeque<>();
	}
	void enque(int data){
		while(!First2.isEmpty() && First2.getLast() > data){
			First2.removeLast();
		}
		First2.addLast(data);
		First1.add(data);
	}

	void deque(){
		if(Objects.equals(First2.getFirst(), First1.peek())){
			First2.removeFirst();
		}
		First1.remove();
	}
	int getMin() throws Exception{
		if(First1.isEmpty())
			throw new Exception("Queue is Empty");
		else
			return First2.getFirst();
	}   
        static void reverse(){ 
             
        Stack<Integer> stack = new Stack<>(); 
        while (!queue.isEmpty()) { 
            stack.add(queue.peek()); 
            queue.remove(); 
        } 
        while (!stack.isEmpty()) { 
            queue.add(stack.peek()); 
            stack.pop(); 
        } 
    }         
        }