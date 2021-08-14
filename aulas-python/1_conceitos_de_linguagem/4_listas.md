# Listas em Python e estruturas de dados análogas

#### Uma lista é uma estrutura de dados que pode ser heterogênea, ou seja,
#### conter mais de um tipo de dados por elemento. Para criar uma lista pode-se
#### fazer de duas formas na inicialização ou por atribuição

###Caraterísticas

* Pode conter elementos repetidos
* Pode conter mais de um tipo de dados;
* Pode ser inicializar com seus valores;
* Pode ser vazia e ter valores adicionados posteriormente;
* Trabalhar com índices nos elementos com valores inteiros baseados em 0;
* Mantem a ordem que os elementos foram adicionados;
* Pode se acessada com índices negativos desde que dentro da faixa de elementos existentes

````
# Listas vazias
l1 = list()
l2 = []

# Atribuição heterogênea:
l3 = [1, 2, 3, "Sapato", "cobra", 2, 3]

# Lista vazia com elemento adicionado através do método append
l2.append("foo")

# Para remover o elemento que acabamos de adicionar e que está posicionado
# no índice 0 basta executar
del l2[0]

# Acessa o primeiro elemento da lista
l3[0]
# Acessa o último elemento da lista
l3[-1]

````

Conceitos de estrutura de dados Pilha e Fila:

Fila: Igual uma fila comum, O primeiro que chega é o primeiro a sair;

Pilha: Como uma pilha de pratos. O último a ser colocado é o primeiro a sair;

Principais métodos da lista:

* append: Adiciona um novo elemento no final da lista;
* clear: Limpa a lista (Apaga todos os elementos);
* copy: Copia os elementos da lista para outra lista;
* count: Conta quantos elementos existem na lista;
* extend: Adiciona uma lista existente dentro de outra lista;
* index: Retorna o índice do elemento, caso exista na lista;
* insert: Adiciona um elemento em dada posição na lista;
* remove: Remove um elemento pelo índice
* reverse: Inverte a ordem da lista;
* sort: Irá ordernar a lista de acordo com o tipo de dados ou função lambda;
* pop: Faz a lista trabalhar como uma pilha, removendo os elementos de cima;
