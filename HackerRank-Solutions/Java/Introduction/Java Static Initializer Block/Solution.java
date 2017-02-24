private static int B;
private static int H;
private static boolean flag;
static Scanner sc = new Scanner(System.in);
static{
    
    B = sc.nextInt();
    H = sc.nextInt();
    if( B<1 || H<1)
    {
        System.out.print("java.lang.Exception: Breadth and height must be positive");
        flag = false;
    }
    else
    {
        flag = true;
    }
}