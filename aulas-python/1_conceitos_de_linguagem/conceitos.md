# Conceitos sobre a linguagem:

## 1 Diferenças entre linguagens

Python é uma linguagem interpretada. O que quer dizer que é necessário uma máquina
virtual para processar a linguagem natural escrita pelo programador em código intermediário,
inteligível pela máquina virtual, que por sua vez irá transformá-lo em código de máquina.

## Linguagens compiladas

Como vocês podem observar o software escrito em C como exemplo necessita ser compilado
para cada **arquitetura de software** que vai rodar. Este é um exemplo de linguagem compilada,
onde a linguagem natural é compilada em bytecode somente uma vez e depois o produto
resultante é um binário

**Vantagens dos softwares compilados:**

* Extremamente rápidos; (Isso é uma característica importante para sistemas de alta precisão);
* Carga inicial demorada (Todo o software é carregado de uma só vez na memória) - Splash Screens;
* Roda com maior eficiência na máquina que é compilado;
* Processo mais confiável pelo fato de ter várias checagens de erro durante a compilação. 

**Desvantagens do softwares compilados**
* Tamanho do bytecode por conta das dependências;
* Processo de compilação mais lento;
* Falta de interoperabilidade; (Softwares compilados em um determinado sistema só rodam nele mesmo)


## 2 Linguagens Interpretadas;

Possuem como características principais o fato de ter uma máquina virtual para poderem ser executadas;
Assim sendo, um software como o do exemplo escrito em C terá a alocação do espaço de memória de acordo
com o sistema operacional e a arquitetura de software que estiver rodando;

**Vantagens:**
* Interoperabilidade; (Capacidade de rodar em diversos dispositivos com o mesmo código);
  * Lema do Java: Write once, run everywhere;
  * Piada de tecnologia: Write once, run the hills!
* Código principal com menor tamanho;
* Mais simples de debuggar;

**Desvantagens:**
* Mais lento;

# Caractererísticas das Linguagens

## Tipagem Estática
* Necessidade: Preciso guardar um número inteiro;
Linguagem de tipagem estática: Definir o tipo da variável na hora da sua criação (instanciação)
Exemplo: Linguagem C ou Java.

## Tipagem Dinâmica
* Necessidade: Preciso guardar um número inteiro;
Linguagem de tipagem dinâmica: Na hora da primeira atribuição, o tipo da variável é defido;
Exemplo: Python


## Fortemente Tipadas
* Não aceitam operaçẽs entre varáveis de tipos diferentes:
Exemplo: Não é possível somar um número inteiro com um número em 
string sem uma coerção de tipo prévia.

## Fracamente Tipadas
* Aceitam operaçẽs entre varáveis de tipos diferentes tentado fazer magia:
Exemplo: JavaScript tenta adivinhar o que você quer 
fazer quando soma um número com uma string com número.

Assim podemos presumir que Python é uma linguagem de tipagem dinâmica e ao mesmo
tempo fortemente tipada.
