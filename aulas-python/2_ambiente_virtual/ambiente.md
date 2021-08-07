# Conceitos sobre ambiente virtual para programação em Python

##1 - O Virtualenv
Como python é uma linguagem interpretada e cada software precisará de um interpretador
para executar surgem alguns problemas.

* Como isolar as aplicações que dependem da mesma biblioteca de software em versões diferentes?
* Como ter códigos legados usando versões antigas do Python rodando ao mesmo tempo com software novo?

Para essa demanda utilizamos o virtualenv, que por sua vez, cria para cada projeto um ambiente virtual 
completamente isolado, a fim de que, o software não conflite com demais projetos em Python.

### Como criar um ambiente virtual:

Utilizando o Linux, instala-se os pacotes base: Em sistemas derivados do Debian (Ubuntu, Mint, etc)

O Python3 em sim

``apt-get install python3``

Os pacotes de desenvolvimento do python

``apt-get install python3-dev``

Em sistemas mais antigos

``apt-get install python-virtualenv``

Para criar o ambiente virtual usa-se

Para sistemas antigos:

``virtualenv -p python3 NOME_DO_AMBIENTE``

Para sistemas mais novos:

``python3 -m venv NOME_DO_AMBIENTE``

### Como ativar um ambiente virtual:

``source ./NOME_DO_AMBIENTE/bin/activate``

### Como desativar um ambiente virtual:

``deactivate``

Para maiores detalhes do projeto:
https://joaodecarvalho.com/pt-br/blog/post/iniciando-um-projeto-django-pronto-para-colaboracao-e-escala/
