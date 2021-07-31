package sec05;

public class PersonExample {
    public static void main(String[] args) {
        Person p1 = new Person("123456-1234567", "최창환");

        System.out.println(p1.nation);
        System.out.println(p1.ssn);
        System.out.println(p1.name);
    }
}
