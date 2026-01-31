package classactivity5;
public class Bank implements Runnable {

    static int balance = 0;

    public synchronized void deposit() {
        balance += 100;
    }

    public synchronized void withdraw() {
        balance -= 100;
    }

    public int getValue() {
        return balance;
    }

    @Override
    public synchronized void run() {
        deposit();
        System.out.println(
            "Value for Thread after deposit " +
            Thread.currentThread().getName() + " " +
            getValue()
        );

        withdraw();
        System.out.println(
            "Value for Thread after withdraw " +
            Thread.currentThread().getName() + " " +
            getValue()
        );
    }
}
