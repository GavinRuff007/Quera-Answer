import java.util.*;
class practice01
{
static String PostFixToInfix(String string)
{
	Stack<String> stack1 = new Stack<String>();
	for (int i = 0; i < string.length(); i++)
	{         
		if (string.charAt(i)>='a' && string.charAt(i) <= 'z')	
		{
		stack1.push(string.charAt(i) + "");
		}
		else
		{
			String op1 = stack1.peek();
			stack1.pop();
			String op2 = stack1.peek();
			stack1.pop();
			stack1.push("(" + op2 + string.charAt(i) + op1 + ")");		
		}
	}
	return stack1.peek();
}
public static void main(String []args){
    String s = "ab+c-";
    System.out.println(PostFixToInfix(s));  
}
}