public class PrototypePatternDemo {
   public static void main(String[] args) {
      ShapeCache.loadCache();

      Shape clonedShape1 = ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape1.getType());		

      Shape clonedShape2 = (Shape) ShapeCache.getShape("2");
      System.out.println("Shape : " + clonedShape2.getType());		

      Shape clonedShape3 = (Shape) ShapeCache.getShape("3");
      System.out.println("Shape : " + clonedShape3.getType());	

	  Shape clonedShape4 = ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape4.getType());	

	  Shape clonedShape5 = ShapeCache.getShape("1");
	  System.out.println("Shape : " + clonedShape5.getType());

	  Shape clonedShape6 = ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape6.getType());	 

	  Shape clonedShape7 = ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape7.getType());	  
   }
}