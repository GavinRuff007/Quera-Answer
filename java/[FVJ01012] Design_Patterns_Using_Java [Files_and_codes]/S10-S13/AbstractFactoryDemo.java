public class AbstractFactoryDemo{
	public static void main(String[] args){
		AbstractFactory shapeFactory = FactoryProducer.getFactory(false);
		Shape sh1 = shapeFactory.getShape("RECTANGLE");
		sh1.draw();
		
		AbstractFactory shapeFactory2 = FactoryProducer.getFactory(true);
		Shape sh2 = shapeFactory2.getShape("RECTANGLE");
		sh2.draw();
	}
}