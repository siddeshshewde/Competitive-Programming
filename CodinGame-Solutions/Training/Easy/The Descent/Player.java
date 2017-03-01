import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        // game loop
        while (true) {
            int largest = 0;
            int ii =0;
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                if (mountainH > largest)
                {
                    ii = i;
                    largest = mountainH;
                }
            }

            System.out.println(ii); // The index of the mountain to fire on.
        }
    }
}