
public class Test {
    public static void main(String[] args) {
        // 打印一条消息到控制台
        System.out.println("Hello, World!");

        // 定义一个变量并打印
        int number = 42;
        System.out.println("The answer to life, the universe, and everything is: " + number);

        // 调用一个方法
        greet("Alice");
        greet("Bob");

        // 定义一个数组并遍历
        String[] names = {"John", "Jane", "Doe"};
        for (String name : names) {
            System.out.println("Hello, " + name + "!");
        }
    }

    // 定义一个方法
    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }
}