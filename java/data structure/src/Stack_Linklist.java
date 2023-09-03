public class Stack_Linklist {
    private Node head;

    private class Node {
        int data;
        Node next;
    }
 
    public Stack_Linklist() {
        head = null;
    }

    public void push(int data) {
        Node prevHead = head;
        head = new Node();
        head.data = data;
        head.next = prevHead;
    }
    
    public int pop() throws LinkedListEmptyException {
        if (head == null) {
            throw new LinkedListEmptyException();
        }
        int data = head.data;
        head = head.next;
        return data;
    }
    public static void main(String args[])
    {
    }
    public static void printList(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.format("%d ", temp.data);
            temp = temp.next;
        }
        System.out.println();
    }
}

class LinkedListEmptyException extends RuntimeException {
    private static final long serialVersionUID = 1L;
 
    public LinkedListEmptyException() {
        super();
    }
 
    public LinkedListEmptyException(String message) {
        super(message);
    }
}
