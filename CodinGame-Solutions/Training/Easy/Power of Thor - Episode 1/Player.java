import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTX = in.nextInt(); // Thor's starting X position
        int initialTY = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.
            if (initialTY < lightY)
            {
                initialTY++;
                System.out.print("S");
            }
            else if (initialTY > lightY)
            {
                initialTY--;
                System.out.print("N");
            }
            if (initialTX < lightX)
            {
                initialTX++;
                System.out.print("E");
            }
            else if (initialTX > lightX)
            {
                initialTX--;
                System.out.print("W");
            }

            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println("");
        }
    }
}