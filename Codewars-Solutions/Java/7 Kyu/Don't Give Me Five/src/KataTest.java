import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class KataTests {
    @Test
    public void exampleTests() {
      assertEquals(8, Kata.dontGiveMeFive(1,9));
      assertEquals(12, Kata.dontGiveMeFive(4,17));
    }
}