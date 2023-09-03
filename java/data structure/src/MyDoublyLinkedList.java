class NodeD {
    public int data;
    public NodeD next;
    public NodeD prev;
    
}
 
public class MyDoublyLinkedList {
 
    private NodeD head;
    private NodeD tail;
    int size;
 
    public void insertFirst(int data) {
        NodeD newNodeD = new NodeD();
        newNodeD.data = data;
        newNodeD.next = head;
        newNodeD.prev=null;
        if(head!=null)
            head.prev=newNodeD;
        head = newNodeD;
        if(tail==null)
            tail=newNodeD;
        size++;
    }

    public void insertLast(int data) {
        NodeD newNodeD = new NodeD();
        newNodeD.data = data;
        newNodeD.next = null;
        newNodeD.prev=tail;
        if(tail!=null)
            tail.next=newNodeD;
        tail = newNodeD;
        if(head==null)
            head=newNodeD;
        size++;
    }

    public NodeD deleteFirst() {
        if (size == 0)
            throw new RuntimeException("Doubly linked list is already empty");
        NodeD temp = head;
        head = head.next;
        head.prev = null;
        size--;
        return temp;
    }

    public NodeD deleteLast() {
 
        NodeD temp = tail;
        tail = tail.prev;
        tail.next=null;
        size--;
        return temp;
    }

    public void deleteAfter(NodeD after) {
        NodeD temp = head;
        while (temp.next != null && temp.data != after.data) {
            temp = temp.next;
        }
        if (temp.next != null)
            temp.next.next.prev=temp;
        temp.next = temp.next.next;
 
    }
 
    public void printLinkedListForward() {
        System.out.println("Printing Doubly LinkedList (head --> tail) ");
        NodeD current = head;
        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
        System.out.println();
    }
    
     public void printLinkedListBackward() {
        System.out.println("Printing Doubly LinkedList (tail --> head) ");
        NodeD current = tail;
        while (current != null) {
            System.out.println(current.data);
            current = current.prev;
        }
        System.out.println();
    }
 
    public static void main(String args[])
    {
    }
}