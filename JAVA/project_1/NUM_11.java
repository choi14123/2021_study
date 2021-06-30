import java.util.Scanner;

public class NUM_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int a = num2 % 10;
        int b = num2 % 100 / 10;
        int c = num2 / 100;
        System.out.println(num1 * a);
        System.out.println(num1 * b);
        System.out.println(num1 * c);
        System.out.println(num1 * num2);
    }
}
