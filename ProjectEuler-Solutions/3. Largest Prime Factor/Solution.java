public class Solution{
	
	public static int largestPrimeFactorOfTheNumber(long number){
		 int i;
		    for (i = 2; i <= number; i++) {
		        if (number % i == 0) {
		            number /= i;
		            i--;
		        }
		    }
		    return i;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int prime=largestPrimeFactorOfTheNumber(600851475143l);
		System.out.println(prime);
	}
}