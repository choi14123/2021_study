import java.util.Scanner;

public class NUM_03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = 0;
        for (int i = 1; i <= N; ++i) {
            A += i;
        }
        System.out.println(A);
    }
}
