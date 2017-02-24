public class Keypad
{
	public static int presses(String phrase)
	{
		int presses=0;
		if (phrase == null)
			return 0;
		for (int i=0;i<phrase.length();i++)
		{
			switch(phrase.charAt(i))
			{
				case 'a': case 'A': case 'd': case 'D': case 'g': case 'G': case 'j': case 'J': case 'm': case 'M': case 'p': case 'P': case 't': case 'T': case 'w': case 'W': case ' ': case '*': case '#': case '1' : presses = presses + 1; break;
				case 'b': case 'B': case 'e': case 'E': case 'h': case 'H': case 'k': case 'K': case 'n': case 'N': case 'q': case 'Q': case 'u': case 'U': case 'x': case 'X': case '0' : presses = presses + 2; break;
				case 'c': case 'C': case 'f': case 'F': case 'i': case 'I': case 'l': case 'L': case 'o': case 'O': case 'r': case 'R': case 'v': case 'V': case 'y': case 'Y' : presses = presses + 3; break;
				case 's': case 'S': case 'Z': case 'z': case '2': case '3': case '4': case '5': case '6': case '8' : presses = presses + 4; break;
				case '7': case '9' : presses = presses + 5; break;
			}
		}
		return presses;
	}
}
