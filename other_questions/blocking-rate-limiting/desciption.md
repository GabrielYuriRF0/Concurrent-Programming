# Blocking rate-limiting
## Em certos sistemas evitamos que requisições de tipos diferentes sejam executadas concorrentemente. Considere o código abaixo:  
```c
func handle(Request req) {
exec(req)
}
```
## Considere que a função handle é executada por uma thread toda vez que uma requisição chega no sistema. Você não precisa se preocupar com a criação dessa thread. Uma requisição tem um tipo inteiro, ou seja, Request.type. Em nosso caso, há dois tipos (0 e 1). Altere o código da função handle para controlar a execução do sistema de maneira que não seja possível a execução concorrente pela função exec de requisições de tipos diferentes. Além disso, controle a quantidade máxima de execuções da função exec segundo um parâmetro N definido a priori. Sua solução terá pontuação máxima caso considere critérios de justiça e evite starvation. De qualquer maneira, uma solução sem esses critérios atendidos é aceitável (declare em sua resposta se você pretende atendê-los).

### Comentários gerais:
- Não mude a função exec;
- Altere o código da função handle para implementar as restrições de
controle de concorrência. Crie funções auxiliares se achar necessário;
- Crie uma função main para iniciar e criar variáveis globais incluindo
semáforos.