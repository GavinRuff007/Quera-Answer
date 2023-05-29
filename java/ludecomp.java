class ludecomp {

	static int MAX = 100;
	static String s = "";
	static void luDecomposition(int[][] mat, int n)
	{
		int[][] lower = new int[n][n];
		int[][] upper = new int[n][n];

		for (int i = 0; i < n; i++)
		{
			for (int k = i; k < n; k++)
			{
				
				int sum = 0;
				for (int j = 0; j < i; j++)
					sum += (lower[i][j] * upper[j][k]);

				upper[i][k] = mat[i][k] - sum;
			}


			for (int k = i; k < n; k++)
			{
				if (i == k)
					lower[i][i] = 1; 
				else
				{
					
					int sum = 0;
					for (int j = 0; j < i; j++)
						sum += (lower[k][j] * upper[j][i]);

					
					lower[k][i]
						= (mat[k][i] - sum) / upper[i][i];
				}
			}
		}

		System.out.println(setw(2) + "	 Lower Triangular"
						+ setw(10) + "Upper Triangular");

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
				System.out.print(setw(4) + lower[i][j]
								+ "\t");
			System.out.print("\t");

			
			for (int j = 0; j < n; j++)
				System.out.print(setw(4) + upper[i][j]
								+ "\t");
			System.out.print("\n");
		}
	}
	static String setw(int noOfSpace)
	{
		s = "";
		for (int i = 0; i < noOfSpace; i++)
			s += " ";
		return s;
	}
	public static void main(String arr[])
	{
		int mat[][] = { {7,2,5 },
						{ -2,7,132 },
						{ 0,3, 8 } };

		luDecomposition(mat, 3);
	}
}

