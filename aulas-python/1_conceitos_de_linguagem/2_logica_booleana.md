# Lógica Booleana e tabela verdade

## Conceito

Operações lógicas entre variáveis para saber de acordo com os operadores 
relacionais, qual a resultante da tabela verdade me questão:

## Operadores Relacionais binários

Português

####E , OU, OU EXCLUSIVO

Inglês

####AND , OR, XOR

Python

and, or, not, ^

##Tabela verdade AND
### Para que a condição entre duas variáveis seja verdadeira é necessário que ambas
### sejam verdadeiras
````
TABELA AND

A        |    B      | Resultado
True     |  True     |   True   
True     |  False    |   False
False    |  True     |   False
False    |  False    |   False
````

##Tabela verdade OR
### Para que o resultado seja verdadeiro pelo menos uma das variáveis deve ser verdadeira

````
TABELA OR

A        |    B      | Resultado
True     |  True     |   True 
True     |  False    |   True
False    |  True     |   True
False    |  False    |   False
````

##Tabela verdade XOR (Ou Exclusivo)
### Para que o resultado seja verdadeiro 

````
TABELA XOR

A        |    B      | Resultado
True     |  True     |   False 
True     |  False    |   True
False    |  True     |   True
False    |  False    |   False
````

##Operadores aritiméticos.

#### Para esses exemplos iremos trabalhar apenas om valores numéricos
#### Para fins de entendimento saibam que exitem precedência de 
#### resolução entre oepradores aritiméticos. Igualzinho na matemática diária

A = 2

B = 3

C = 5

D = 4

expressao = (((A * C) - (B / A)) * B) + D

## Exemplo: Cálculo de juros simples

````
valor_divida = 435.87
taxa_juros_dia = 0.33%
atraso_dias = 45

# Regra de três
#435.87 -----> 100%
#x      -----> 0.33%

# Calculo dos juros diários com base na regra de três simples
valor_juros_dia = (valor_divida * taxa_juros_dia) / 100
# 1.4383710000000003

# Calculo dos juros multiplicados pelos dias de atraso
valor_juros_total = valor_juros_dia * atraso_dias
#64.726695

# Calculo do valor corrigido
valor_corrigido = valor_divida + valor_juros_total
# 500.596695
````

## Operadores Relacionais

````
>  | Maior que
<  | Menor que
>= | Maior ou igual
<= | Menor ou igual
== | Compara os valores como sendo iguais entre variáveis
!= | Compara os valores como sendo diferentes entre variáveis

````

## Exemplos
````
1 > 2 # False
1 < 2 # True
2 >= 2 # True
1 <= 2 # True

1 > 2 or 10 % 2 == 0 # True
1 == 2 and 1 == 1 # False
1 == 2 or 1 == 1 # True
````
