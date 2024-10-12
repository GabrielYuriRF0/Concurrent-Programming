import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.LinkedList;

public class Sum {

    public static int sum(FileInputStream fis) throws IOException {
        
	int byteRead;
        int sum = 0;
        
        while ((byteRead = fis.read()) != -1) {
        	sum += byteRead;
        }

        return sum;
    }

    public static long sum(String path) throws IOException {

        Path filePath = Paths.get(path);
        if (Files.isRegularFile(filePath)) {
       	    FileInputStream fis = new FileInputStream(filePath.toString());
            return sum(fis);
        } else {
            throw new RuntimeException("Non-regular file: " + path);
        }
    }

    public static void main(String[] args) throws Exception {

        if (args.length < 1) {
            System.err.println("Usage: java Sum filepath1 filepath2 filepathN");
            System.exit(1);
        }

	//many exceptions could be thrown here. we don't care
        List<Task> tasks = new LinkedList<Task>();
        List<Thread> threads = new LinkedList<Thread>();
        for (String path : args) {
            //long sum = sum(path);
            //System.out.println(path + " : " + sum);
            Task t = new Task(path);
            Thread currentThread = new Thread(t, "thread of " + path);
            currentThread.start();
            tasks.add(t);
            threads.add(currentThread);
        }

        // join for all
        for (Thread t : threads) {
            t.join();
        }

        // printing
        for (Task t : tasks) {
            System.out.println(t.getPath() + " : " + t.getSum());
        }
    }
}
