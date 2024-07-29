# Concurrent Linked list: Abaixo, temos um esboço de implementação de lista encadeada. Esta implementação tem problemas de concorrência. Detecte e corrija os problemas detectados usando semáforos. Não proteja regiões maiores que o necessário.
``` c
// tipo node
typedef struct __node_t {
int key;
struct __node_t *next;
} node_t;

// basic list structure
typedef struct __list_t {
node_t *head;
} list_t;

void List_Init(list_t *L) {
L->head = NULL
}

int List_Insert(list_t *L, int key) {
node_t* new = malloc(sizeof(node_t));
if (new == NULL) {
perror("malloc");
return -1; // fail
}
new->key = key;
new->next = L->head;
L->head = new;
return 0; // success
}

int List_Lookup(list_t*L, int key) {
node_t*curr = L->head;
while (curr) {
if (curr->key == key){
return 0; // success
}
curr =curr->next;
}
return -1; // failure
}
```
