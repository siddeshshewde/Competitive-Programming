import java.io.BufferedReader;
import java.io.InputStreamReader;

class ToggleString
{
    public static void main(String args[] ) throws Exception
   {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String text = br.readLine();
    char[] chars = text.toCharArray();
    for (int i = 0; i < chars.length; i++)
    {
        char c = chars[i];
        if (Character.isUpperCase(c))
        {
            chars[i] = Character.toLowerCase(c);
        }
        else if (Character.isLowerCase(c))
        {
            chars[i] = Character.toUpperCase(c);
        }
    }
    System.out.print(chars);
}
}