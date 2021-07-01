import java.util.Scanner;

public class NUM_05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        if(M < 45) {
            H -= 1;
            M = 60 - (45 - M);
            if(H < 0) {
                H = 23;
            }
            System.out.println(H + " " + M);
        }
        else {
            System.out.println(H + " " + (M - 45));
        }
}
}
