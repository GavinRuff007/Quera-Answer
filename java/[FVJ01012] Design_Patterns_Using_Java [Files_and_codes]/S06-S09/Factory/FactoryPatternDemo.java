public class FactoryPatternDemo{
	public static void main(String[] args){
		ShapeFactory shapeFactory = new ShapeFactory();
		
		Shape sh1 = shapeFactory.getShape("SQUARE");
		sh1.draw();
		
		Shape sh2 = shapeFactory.getShape("RECTANGLE");
		sh2.draw();
		
		
		Shape sh3 = shapeFactory.getShape("CIRCLE");
		sh3.draw();
		
		Shape sh4 = shapeFactory.getShape("TRIANGLE");
		sh4.draw();
		
	}
}