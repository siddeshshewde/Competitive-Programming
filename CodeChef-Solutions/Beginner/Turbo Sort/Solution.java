import java.util.*;
class tsort
{
public static void main(String ar[])
{
Scanner i=new Scanner(System.in);
int n=i.nextInt();
int a[]=new int[n];
for(int x=0;x<n;x++)
a[x]=i.nextInt();
Arrays.sort(a);
for(int x=0;x<n;x++)
System.out.println(a[x]);
}
}