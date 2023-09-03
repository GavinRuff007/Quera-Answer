public class BuilderDesignPattern
{
	public static void main(String[] args)
	{
		User user1 = new User.UserBuilder("Mohammad" , "Abdollahi")
		.age(39)
		.phone("3939")
		.address("Tehran")
		.build();
		
		System.out.println(user1);
		
		User user2 = new User.UserBuilder("Ali" , "Alavi")
		.age(20)
		.phone("1234")
		//.address("Tehran")
		.build();
		
		System.out.println(user2);
		
		User user3 = new User.UserBuilder("Ali" , "Alavi")
		//.age(20)
		//.phone("1234")
		//.address("Tehran")
		.build();
		
		System.out.println(user3);
	}
}