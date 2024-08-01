public class Main{
    
}
class BufferedQueue{
    private int capacity;
    private final Queue<T> queue;

    public BufferedQueue(int capacity){
        this.capacity = capacity;
        this.queue = new LinkedList<>();
    }

    public T dequeue(){
        T item = queue.poll();
        return item;

    }

    public void enqueue(T item){
        this.queue.add(item);
    }





}