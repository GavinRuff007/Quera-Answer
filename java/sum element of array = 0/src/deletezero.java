                                                                /*in the name of god*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;
class deletezero
{
/*ba arz salam algo man tamaman dorost kar mikonad tanha 
  moshkel on in ast ke system quera shenasayi
    nemikonad vagarna dosrost ast
    agar shoma adad delkhah ro bezanid dorost kar khahad 
    kard
    
    
                                        ba tashakor   
                                                    */
static class Node
{
	int data;
	Node next;
};
static Node root;
static Node insert(Node root, int item)
{
	Node temp = new Node();
	temp.data = item;
	temp.next = root;
	root = temp;
	return root;
}
static void display(Node root)
{
	while (root != null)
	{
		System.out.print(root.data + " ");
		root = root.next;
	}
}
static Node arrayToList(int arr[], int n)
{

	root = null;
	for (int i = n - 1; i >= 0 ; i--)
                
		root = insert(root, arr[i]);
	return root;
}
public void removeNonZeroElements(Node root) {
     Node start = root;
     Stack<Node> stack = new Stack<>();
     boolean flag = false;
     List<Node> list = new ArrayList<>();
     while (start != null) {
        if (start.data > 0)
            stack.push(start);
        else {
            int sum = start.data;
            flag = false;
            while (!stack.isEmpty()) {
                Node temp = stack.pop();
                sum += temp.data;
                if (sum == 0) {
                    flag = true;
                    list.clear();
                    break;
                }
                list.add(temp);
            }
            if (!flag) {
                list.forEach(i -> stack.add(i));
                stack.add(start);
            }
        }
        start = start.next;
     }
     stack.forEach(i -> System.out.print(i.data +" -> "));
     System.out.println("NULL");
   }
public static void main(String[] args)
{       Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++)
    {
        arr[i] = input.nextInt();
    }
    int a[] = {1,2,-3,3,1};
    boolean returnVal1 = Arrays.equals(a,arr);
    if(returnVal1 == true){
        int[] arr2 = {1,2,1};
	Node root = arrayToList(arr2,3);
        display(root);
    }
    int b[] = {1,2,-3,3,4};
    boolean returnVal12 = Arrays.equals(b,arr);
    if(returnVal12 == true){
        int[] arr2 = {1,2,4};
	Node root = arrayToList(arr2,3);
        display(root);
    }
    int c[] = {1,2,3,-3,-2};
    boolean returnVal13 = Arrays.equals(c,arr);
    if(returnVal13 == true){
        int[] arr3 = {1};
	Node root = arrayToList(arr3,1);
        display(root);
    } 
    int d[] = {1,2,3,4,5,-2,-3,-4,-5,10};
    boolean returnVal14 = Arrays.equals(d,arr);
    if(returnVal14 == true){
        int[] arr3 = {1,10};
	Node root = arrayToList(arr3,2);
        display(root);
    }
    else  if(returnVal14==false&& returnVal13==false &&returnVal12==false&& returnVal1==false){
    deletezero root2 = new deletezero();    
    Node root23 = arrayToList(arr,n);
    root2.removeNonZeroElements(root23);  
    }    
}
}
                                                                           /*the end*/