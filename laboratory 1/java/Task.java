import java.io.IOException;

public class Task implements Runnable {

    String path;
    long sum;

    public Task(String path) {
        this.path = path;
        this.sum = 0;
    }

    @Override
    public void run() {
        try {
            this.sum = Sum.sum(this.path);
        } catch (IOException e) {
            //throw new InterruptException();
        }
    }

    public long getSum() {
        return this.sum;
    }

    public String getPath() {
        return this.path;
    }
}
