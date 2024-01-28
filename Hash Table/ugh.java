import java.util.*;

public class HB {
    public static void main(String arg[]) {
        Scanner in = new Scanner(System.in);
        long num = in.nextLong();
        long temp = num;
        long size = 0;
        while (temp != 0) {
            temp /= 10;
            size++;
        }
        temp = num;

        long[] odd = new long[(int) size];
        int index = 0;
        for (long i = size - 1; i >= 0; i--) {
            long digit = temp % 10;
            if (digit % 2 != 0) {
                odd[index++] = digit;
            }
            temp /= 10;
        }

        for (long j = index - 1; j > 0; j--) {
            System.out.print(odd[(int) j]);
        }
    }
}
