# O primeiro problema econtradado é no método List_Insert, pois se garantimos que somente uma thread por vez, pode realizar aS operações new->next = L->head; L->head = new;, podemos ter referências inconsistentes.

# O segundo problema por sua vez, é resultados incorrentos devido a uma inserção que acontence no mesmo tempo de uma busca.

``` c
mutex = Semaphore(1)

// tipo node
typedef struct __node_t {
int key;
struct __node_t *next;
} node_t;

// basic list structure
typedef struct __list_t {
node_t *head;
pthread_mutex_t lock;
} list_t;

void List_Init(list_t *L) {
L->head = NULL;
pthread_mutex_init(&L->lock, NULL);
}

int List_Insert(list_t *L, int key) {
node_t* new = malloc(sizeof(node_t));
if (new == NULL) {
perror("malloc");
return -1; // fail
}
new->key = key;
pthread_mutex_lock(&L->lock);
new->next = L->head;
L->head = new;
pthread_mutex_unlock(&L->lock)
return 0; // success
}

int List_Lookup(list_t*L, int key) {
pthread_mutex_lock(&L->lock);
node_t*curr = L->head;
while (curr) {
if (curr->key == key){
    pthread_mutex_unlock(&L->lock)
return 0; // success
}
curr =curr->next;

}
pthread_mutex_unlock(&L->lock)
return -1; // failure
}
```
