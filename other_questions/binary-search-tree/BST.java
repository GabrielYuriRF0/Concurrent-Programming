public class BST {

    private Node root;
    
    public boolean isEmpty() {
        return this.root == null;
    }

    public void add(int element) {
        
        if (isEmpty())
            this.root = new Node(element);
        else {
                
            Node aux = this.root;
                
            while (aux != null) {
                    
                if (element < aux.value) {
                    if (aux.left == null) { 
                        Node newNode = new Node(element);
                        aux.left = newNode;
                        return;
                    }
                        
                    aux = aux.left;
                } else {
                    if (aux.right == null) { 
                        Node newNode = new Node(element);
                        aux.right = newNode;
                        return;
                    }
                        
                    aux = aux.right;
                }
            }
        }
            
    }
    
}


class Node {
    
    int value;
    Node left;
    Node right;
    
    Node(int v) {
        this.value = v;
    }
    
}
