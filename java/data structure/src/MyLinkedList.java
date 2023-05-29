class Node {
    public int data;
    public Node next;
}
 
public class MyLinkedList {
    private Node head;

    public void insertFirst(int data) {
        Node newHead = new Node();
        newHead.data = data;
        newHead.next = head;
        head = newHead;
    }
    
    public Node deleteFirst() {
        Node temp = head;
        head = head.next;
        return temp;
    }
    
    public void deleteAfter(Node after) {
        Node temp = head;
        while (temp.next != null && temp.data != after.data) {
            temp = temp.next;
        }
        if (temp.next != null)
            temp.next = temp.next.next;
    }

    public void insertLast(int data) {
        Node current = head;
        while (current.next != null) {
            current = current.next; 
        }
        Node newNode = new Node();
        newNode.data = data;
        current.next = newNode;
    }
    public void printLinkedList() {
        System.out.println("Printing LinkedList (head --> last) ");
        Node current = head;
        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
        System.out.println();
    }
 
    public static void main(String args[])
    {
    }
} 
    
    
    
    
    
    
    
    
    
    
    
    

    