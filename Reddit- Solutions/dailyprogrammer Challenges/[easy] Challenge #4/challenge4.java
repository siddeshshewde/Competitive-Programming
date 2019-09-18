import java.util.Scanner;
import java.util.Random;

public class OPT
{
	public static void main (String args[])
	{
		Scanner sc = new Scanner(System.in);
		Random rand = new Random();

		System.out.println("Entern the length of OTP : ");

		//length of OTP
		int length = sc.nextInt();
		String smallChars = "abcdefghijklmnopqrstuvwxyz";
		String capitalChars = smallChars.toUpperCase();
		String numbers = "0123456789";
		String specialChars = "!@#$%^&*_=+-/.?<>)";

		//All possible values
		String values = smallChars + capitalChars + numbers + specialChars;

		//Generating OTP using Random()
		char otp[] = new char[length];

		for (int i = 0 ; i < length ; i++)
		{
			otp[i] = values.charAt(rand.nextInt(values.length()));
		}

		//Printing the unique OTP
		System.out.println(otp);
	}
}